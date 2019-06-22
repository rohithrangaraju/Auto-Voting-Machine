from flask import Blueprint, jsonify, request
from request_data import get_payload
import random
import requests
import string
from blueprints.blueprints_voters import NO_OF_CANDIDATES
import shelve
import collections
from async_functions import initiate_voters
from flask import current_app as app


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    election_number = ''.join(random.choice(chars) for _ in range(size))
    return election_number


url_coordinator = Blueprint(__name__, "coordinator")


def save(data, election_id):
    if not isinstance(data, collections.defaultdict):
        data = data.json()
    with shelve.open("databases/{election_id}".format(election_id=election_id), 'c') as no_sql:
        try:
            no_sql[str(data['wanted_candidate'])] += 1
        except KeyError:
            no_sql[str(data['wanted_candidate'])] = 1


def get_draw_candidates(candidates):
    current_vote = None
    draw_list = []
    for candidates, votes in candidates:
        if not current_vote:
            current_vote = votes
            draw_list.append(candidates)
        elif current_vote == votes:
            draw_list.append(candidates)
        else:
            break
    if len(draw_list) > 1:
        return True, draw_list, current_vote
    return False, draw_list, None


def get_winner(election_id):
    elected_candidates = {}
    with shelve.open("databases/{election_id}".format(election_id=election_id)) as no_sql:
        for candidate in no_sql.keys():
            elected_candidates[candidate] = no_sql[candidate]
    sorted_candidates = sorted(elected_candidates.items(), key=lambda kv: (kv[1], int(kv[0])), reverse=True)
    status, draw_list, drawn_votes = get_draw_candidates(sorted_candidates)
    if status:
        app.logger.info(
            "Draw between list of candidates with ID's {0} and with number of votes {1} for the election id {2}".format(
                draw_list,
                drawn_votes, election_id))
        app.draw = (True, draw_list, drawn_votes)
        initiate_voters(draw=True, election_number=election_id, draw_list=draw_list, voters_count=NO_OF_CANDIDATES)
        return get_winner(election_id)
    else:
        app.logger.info(
            "The winner for the election ID {0} is {1} candidate with total votes {2}".format(election_id,
                                                                                              sorted_candidates[0][0],
                                                                                              sorted_candidates[0][1]))
        temp_data = {"candidate": sorted_candidates[0][0], "total votes": sorted_candidates[0][1]}
        if app.draw[1]:
            temp_data.update({"draw_list": app.draw[1], "drawn_votes": app.draw[2]})
            app.draw = (False, None, None)
        return temp_data


@url_coordinator.route("/coordinator", methods=["GET", "POST"])
def coordinator():
    # election_id = id_generator()
    if request.method == "GET":
        election_id = id_generator()
        app.logger.info("Generated a {0} election number".format(election_id))
        candidate_api = random.randrange(1, NO_OF_CANDIDATES + 1)
        app.logger.info(
            "Coordinator API called and new election ID is {0} and random selected candidate from total {1} candidates is {2}".format(
                election_id, NO_OF_CANDIDATES, candidate_api))
        data = requests.post("http://127.0.0.1:5000/{candidate_api}".format(candidate_api=candidate_api),
                             data={"election_number": election_id})

        save(data, election_id)
        data = data.json()
        temp_data = {}
        temp_data['initiator_number'] = candidate_api
        temp_data['election_number'] = data['election_number']
        return jsonify(temp_data)
    elif request.method == "POST":
        data = get_payload()
        save(data, data['election_number'])
        return jsonify(data)


@url_coordinator.route("/winner/<election_number>", methods=["GET"])
def winner(election_number):
    app.logger.info("Winner API called for the election number {0}".format(election_number))
    data = get_winner(election_number)
    return jsonify(data)

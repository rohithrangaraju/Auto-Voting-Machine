import sys

generator_file = open("blueprints/blueprints_voters.py", "w")

import_functions = """
from flask import Blueprint, jsonify, request
from flask import current_app as app
import random
import requests

from request_data import get_payload
from async_functions import initiate_voters

url_voter = Blueprint(__name__, "voters")
NO_OF_CANDIDATES = {candidate_count}
"""

gen_functions = """
\n
@url_voter.route("/{candidate_number}", methods=["GET", "POST"])
@url_voter.route("/{candidate_number}/<election_number>", methods=["GET", "POST"])
@url_voter.route("/{candidate_number}/user/<election_number>", methods=["GET", "POST"])
def candidate_{candidate_number}(election_number=None):
    data = get_payload()
    url = str(request.url_rule)
    
    if "<election_number>" in url and "user" not in url and app.draw[0]:
        wanted_candidate = random.choice(app.draw[1])
        json_data = dict([("election_number", election_number), ("wanted_candidate", wanted_candidate)])
        data = requests.post("http://127.0.0.1:5000/coordinator",
                             data=json_data)
        return "Voted"
    elif "<election_number>" in url and "user" not in url:
        
        wanted_candidate = random.randrange(1, NO_OF_CANDIDATES + 1)
        selected_candidate = int(url.split("/")[1])
        app.logger.info(
            "Internal API called with candidate ID "+str(selected_candidate)+" and this candidate choose "+str(wanted_candidate)+" candidate ID")
        json_data = dict([("election_number",election_number), ("wanted_candidate",wanted_candidate)])
        data = requests.post("http://127.0.0.1:5000/coordinator",
                             data=json_data)
        return "Voted"
    elif "user" in url:
        wanted_candidate = int(url.split("/")[1])
        app.logger.info(
            "External API called by the user and the choosen candidate is "+str(wanted_candidate)+" candidate ID")
        json_data = dict([("election_number", election_number), ("wanted_candidate", wanted_candidate)])
        data = requests.post("http://127.0.0.1:5000/coordinator",
                             data=json_data)
        return "Your vote is succefull"
    else:
        app.pool.apply_async(initiate_voters, [int(request.url[-1]), data["election_number"], NO_OF_CANDIDATES])
        wanted_candidate = random.randrange(1, NO_OF_CANDIDATES + 1)
        json_data = dict([("candidate_number", NO_OF_CANDIDATES), ("wanted_candidate", wanted_candidate)])
        data.update(json_data)
        return jsonify(data)

\n
"""

cmd_arguments = sys.argv[1]
if ("candidates" in cmd_arguments):
    candidates = cmd_arguments.split("=")[1]
NO_OF_CANDIDATES = int(candidates)

for route in range(1, NO_OF_CANDIDATES + 1):
    test_string = gen_functions
    if route == 1:
        test_string = import_functions + test_string
        test_string = test_string.format(candidate_count=NO_OF_CANDIDATES, candidate_number=route)
    generator_file.write(test_string.format(candidate_number=route))
generator_file.close()

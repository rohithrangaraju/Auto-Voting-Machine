
from flask import Blueprint, jsonify, request
from flask import current_app as app
import random
import requests

from request_data import get_payload
from async_functions import initiate_voters

url_voter = Blueprint(__name__, "voters")
NO_OF_CANDIDATES = 10



@url_voter.route("/1", methods=["GET", "POST"])
@url_voter.route("/1/<election_number>", methods=["GET", "POST"])
@url_voter.route("/1/user/<election_number>", methods=["GET", "POST"])
def candidate_1(election_number=None):
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






@url_voter.route("/2", methods=["GET", "POST"])
@url_voter.route("/2/<election_number>", methods=["GET", "POST"])
@url_voter.route("/2/user/<election_number>", methods=["GET", "POST"])
def candidate_2(election_number=None):
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






@url_voter.route("/3", methods=["GET", "POST"])
@url_voter.route("/3/<election_number>", methods=["GET", "POST"])
@url_voter.route("/3/user/<election_number>", methods=["GET", "POST"])
def candidate_3(election_number=None):
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






@url_voter.route("/4", methods=["GET", "POST"])
@url_voter.route("/4/<election_number>", methods=["GET", "POST"])
@url_voter.route("/4/user/<election_number>", methods=["GET", "POST"])
def candidate_4(election_number=None):
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






@url_voter.route("/5", methods=["GET", "POST"])
@url_voter.route("/5/<election_number>", methods=["GET", "POST"])
@url_voter.route("/5/user/<election_number>", methods=["GET", "POST"])
def candidate_5(election_number=None):
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






@url_voter.route("/6", methods=["GET", "POST"])
@url_voter.route("/6/<election_number>", methods=["GET", "POST"])
@url_voter.route("/6/user/<election_number>", methods=["GET", "POST"])
def candidate_6(election_number=None):
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






@url_voter.route("/7", methods=["GET", "POST"])
@url_voter.route("/7/<election_number>", methods=["GET", "POST"])
@url_voter.route("/7/user/<election_number>", methods=["GET", "POST"])
def candidate_7(election_number=None):
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






@url_voter.route("/8", methods=["GET", "POST"])
@url_voter.route("/8/<election_number>", methods=["GET", "POST"])
@url_voter.route("/8/user/<election_number>", methods=["GET", "POST"])
def candidate_8(election_number=None):
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






@url_voter.route("/9", methods=["GET", "POST"])
@url_voter.route("/9/<election_number>", methods=["GET", "POST"])
@url_voter.route("/9/user/<election_number>", methods=["GET", "POST"])
def candidate_9(election_number=None):
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






@url_voter.route("/10", methods=["GET", "POST"])
@url_voter.route("/10/<election_number>", methods=["GET", "POST"])
@url_voter.route("/10/user/<election_number>", methods=["GET", "POST"])
def candidate_10(election_number=None):
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




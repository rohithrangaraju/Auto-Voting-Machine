from flask import jsonify




def response_candidate(candidate_number=None):
    data_voter = {"candidate_number":candidate_number}
    return jsonify(data_voter)
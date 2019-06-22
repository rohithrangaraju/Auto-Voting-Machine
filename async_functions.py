import requests
import asyncio
import random


def initiate_voters(current_voterid=None, election_number=None, voters_count=None, draw=False, draw_list=None):
    candidates_list = list(range(1, voters_count + 1))
    random.shuffle(candidates_list)
    for candidate_number in candidates_list:
        if not draw and candidate_number != current_voterid:
            requests.get("http://127.0.0.1:5000/{candidate_number}/{election_number}".format(
                candidate_number=candidate_number, election_number=election_number))
        elif draw and candidate_number not in draw_list:
            requests.get("http://127.0.0.1:5000/{candidate_number}/{election_number}".format(
                candidate_number=candidate_number, election_number=election_number))

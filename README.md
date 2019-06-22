##Voting Machine

_This project is about generating election participants and elect them using application(randomly) or by the user._

**PROJET SETUP**

######**First install necessary requirements from requirements.txt**
`pip install -r requirements.txt`

######**Generate no of pariticipants for the election**
`python candidate_generator.py candidates=<no_of_candidates>`

`Example: python candidate_generator.py candidates=10`
All the candidates are generated in sequential manner 1 to no_of_candidates
######**Start the application**
`python VotingMachine.py`

######**Necessary URLs**
To initiate the elections call the coordinator api using browser or postman(GET REQUEST)

`http://127.0.0.1:5000/coordinator`

To vote a particular candidate

`http://127.0.0.1:5000/<candidate-number>/user/<election_number>`

To get the winner

`http://127.0.0.1:5000/winner/<election_number>`

**NOTE**

The tie breaker algorithm is when candidates get similar votes the candidate with max candidate id will be elected.

The data is persisted using **shelve**. This stores key value pairs in a file, instead of a mysql database. i have used 
nosql database format.

All the data is stored inside databases folder with election number as its unique ID.

The output is displayed in JSON format.
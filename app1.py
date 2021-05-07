from flask import Flask,request
import requests
from flask import jsonify
import json
# import firebase_admin
# from firebase_admin import credentials,firestore

# from flask_cors import CORS,cross_origin

import json
app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    response =  jsonify("Hello World Route working All good to go")
    return response

@app.route('/symptoms',methods=['GET'])
def symptoms():
    res = requests.request("GET", 'https://sandbox-healthservice.priaid.ch/symptoms?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJhbnNhbG1hbnZlbmRyYUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjkwNjYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMjEtMDUtMDciLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTYyMDQzMjMzNCwibmJmIjoxNjIwNDI1MTM0fQ.kqPV670JRLEipulTeJDNrk9E3ckc_J8RBr9hr0iVmdE&language=en-gb&format=json')
    # req = request.get_json()
    # resp=json.dumps(res)
    print(res.text)
    # return jasonify(resp)
    # response1 =  jsonify("Hello World Route working All good to go")
    return res.text

# @app.route('/details', methods = ['GET'])
# def detail():
#     # req = request.get_json()
#     req = {
#         gender : 'male',
#         age : 2000
#     }
#     gender = req.gender
#     age = req.age
#     return {gender,age}

@app.route('/diagnosis',methods=['GET'])
def diagnosis() :
    # req = request.get_json()
    symp_id = 10
    gender = 'male'
    age = 2000
    # res1 = requests.request("GET",'/details')
        # gender = res1.text.gender
        # age  = res1.text.age
    res = requests.request("GET",'https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=['+str(symp_id)+']&gender='+gender+'&year_of_birth='+str(age)+'&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJhbnNhbG1hbnZlbmRyYUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjkwNjYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMjEtMDUtMDciLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTYyMDQzNDk5OSwibmJmIjoxNjIwNDI3Nzk5fQ.b32C0cPEAZBAITMg79J4eF1-u2eJJNwdWZTI6vEoUpE&format=json&language=en-gb')
    return res.text

@app.route('/issue', methods = ['GET'])
def issue():
    issue_id = 495
    res = requests.request("GET", 'https://sandbox-healthservice.priaid.ch/issues/'+str(issue_id)+'/info?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJhbnNhbG1hbnZlbmRyYUBnbWFpbC5jb20iLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL3NpZCI6IjkwNjYiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMjEtMDUtMDciLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTYyMDQzNTYxNCwibmJmIjoxNjIwNDI4NDE0fQ.xjK5USLP3SlR50fv8G46p_JUWFwFawotfBZKhCdbr1w&format=json&language=en-gb')
    return res.text
    
if __name__ == '__main__':
    app.run(debug=True,port=3000)
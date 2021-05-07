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
    print(res)
    # return jasonify(resp)
    response1 =  jsonify("Hello World Route working All good to go")
    return response1


if __name__ == '__main__':
    app.run(debug=True,port=3000)
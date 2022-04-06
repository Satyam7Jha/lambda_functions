import json
from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb+srv://user:user@cluster0.vgvn2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def lambda_handler(event, context):
    usn = event["queryStringParameters"]['usn']


    tem = {usn:"True",
       "Date": str(datetime.now()).split()[0],
       "Time":str(datetime.now()).split()[1]
    }
    db = client.get_database('CollegeConnect')
    table = db.EnrolledUsers
    table.insert_one(tem)
    return {
        "statusCode": 200,
        'headers': {
            "Content-Type" : "application/json",
            "Access-Control-Allow-Origin" : "*",
            "X-Requested-With" : "*",
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Methods" : "OPTIONS,POST,GET"
        },
        # "body": json.dumps({"message":"user enrolled"})
    }

# lambda_handler(4,4)
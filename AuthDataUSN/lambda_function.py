import json
from pymongo import MongoClient
import random




client = MongoClient("mongodb+srv://user:user@cluster0.vgvn2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")





def lambda_handler(event, context):


    db = client.get_database('CollegeConnect')
    records = db.News
    table = db.StudentInfo
    x,y= "Primary Email Id (Provide active personal Email ID as this ID will be used for all further communications)","Secondary Email ID (This email ID will be used if required, otherwise all communication will be sent to primary ID)"

    data = list(table.find({},{"Roll No",x,y,"Name"}))


    clientData = {}
    for i in data:

        
        if 'Roll No' in i:
            
            
            tem = {"Name":i["Name"],"Email":[i[x],i[y]],"otp" : random.randint(1111,9999)}
           
            clientData[i['Roll No']] = tem
    
    return {
        "statusCode": 200,
        'headers': {
            "Content-Type" : "application/json",
            "Access-Control-Allow-Origin" : "*",
            "X-Requested-With" : "*",
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Methods" : "OPTIONS,POST,GET"
        },
        "body": clientData
    }


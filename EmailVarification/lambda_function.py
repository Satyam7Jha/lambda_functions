import json
import smtplib
from pymongo import MongoClient

def lambda_handler(event, context):
   
    email = event["queryStringParameters"]['email']
    otp = event["queryStringParameters"]['otp']
    




    gmail_user = "collegeconnect77@gmail.com"
    gmail_password = "8618660526d"

    sent_from = gmail_user
    to = [email]
    subject = 'Varification Code for CollegeConnect'
    body = 'OTP-{}'.format(otp)

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    return {
    "statusCode": 200,
    'headers': {
        "Content-Type" : "application/json",
        "Access-Control-Allow-Origin" : "*",
        "X-Requested-With" : "*",
        "Access-Control-Allow-Headers" : "Content-Type",
        "Access-Control-Allow-Methods" : "OPTIONS,POST,GET"
    },
    "body": json.dumps({"message" : "otp send sucessfully"})
    }
        
   

from flask import Flask
from datetime import datetime
import requests
import os
import smtplib
import imghdr
import json
import time
import yaml
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from email.message import EmailMessage



def whattsappTakeover():



    #configurations need to read from configurations.yaml file
    # with open("spreadsheetFunctions/configurations.yaml", "r") as ymlfile:
    #     cfg = yaml.load(ymlfile)

    #reading instance id   
    instanceid="instance294124"

    url = "https://api.chat-api.com/"+ str(instanceid)+ "/takeover?token=bfllgpii7xqb42zq"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if str(json.loads(response.text)['result'])=='Takeover request sent to WhatsApp':
        print("Instance takingover taking place , will take around 4-5 seconds")
        time.sleep(5)
    
    print("Whattsapp instance is activated")

    return 

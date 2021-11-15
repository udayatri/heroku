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



def isOnWhattsapp(number):

    if str(number[0])=='+':
        number = number[1:]
        
    if len(number)==10:
        number='91'+ str(number)


    try: 
        url = "https://api.chat-api.com/instance294124/checkPhone?token=bfllgpii7xqb42zq&phone=" + str(number) 
    
        payload={}
        headers = {}
        
        response = requests.request("GET", url, headers=headers, data=payload)
        
        
        json_data = json.loads(response.text)['result']
        
        if json_data=='not exists':
            return False
    
    
        return True    
        
    except:
        return False



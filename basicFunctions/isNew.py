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




def isNew(number,email):

    scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds =ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open("personal Dev").worksheet("Completed Session")
    data = spreadsheet.get_all_values()
    
    values=data[1:]
    
    for entry in values:
        if str(entry[2])==number or str(entry[3])==email:
            return entry[5]


    return True
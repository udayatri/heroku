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
from basicFunctions.isOnWhattsapp import isOnWhattsapp
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from email.message import EmailMessage




def firstMsg1(name,number,number1):
    url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Hi " + str(name.title()) + " " + str(number1) +"\\n its working\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
    headers = {
            'Content-Type': 'application/json'
            }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return


def firstMsg(name,number):
    url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"

    payload="{\r\n  \"body\": \"Hi " + str(name.title()) + "\\nYou registered for the interactive session with Drivekraft and here we are as promised \xF0\x9F\x98\x83 . \\n\\nIt's great that you are ready to talk and remember it's never too late.\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
    headers = {
            'Content-Type': 'application/json'
            }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return
    

def sendLink(name,number):
    
    url = "https://api.chat-api.com/instance294124/sendLink?token=bfllgpii7xqb42zq"
    
    payload="{\r\n  \"body\": \"https://forms.gle/dFdsNJMErDgeauWy5\",\r\n  \"previewBase64\": \"nn\",\r\n  \"title\": \"Follow up form\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
    headers = {
      'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    return


def SecondMsg(name,number):
    url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"
    
    payload="{\r\n  \"body\": \"Can you please this above form\xF0\x9F\x98\x83 \\n\\nThis will help to know more about you and assign you the best match of psychologist \xF0\x9F\x98\x87 \xF0\x9F\x98\x87 \\n\\nDo let me know once you filled the form , I will proceed with schedule it\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
    headers = {
      'Content-Type': 'application/json'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    print(response.text)
    return

def send_Message(name,number):
    
    if str(number[0])=='+':
        number = number[1:]
        
    if len(number)==10:
        number='91'+ str(number)

    if isOnWhattsapp(number)==False:
        return False
        
    firstMsg(name,number)
    sendLink(name,number)
    SecondMsg(name,number)
     
    return

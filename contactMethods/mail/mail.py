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




def send_mail(name,reciever):

    EMAIL_ADDRESS = "drivekraft@gmail.com"
    EMAIL_PASSWORD = 'kxgudynwonausuqh'
    
    msg1="Hi " + str(name)+" \nYou registered for the interactive session with Drivekraft and here we are as promised 😃 .  \nIt's great that you are ready to talk and remember it's never too late."
    
    msg2="\n\n https://forms.gle/dFdsNJMErDgeauWy5"
    
    msg3="\n\nCan you please this above form😃  \nThis will help to know more about you and assign you the best match of psychologist 😇 😇  \n\nDo let us know once you filled the form , I will proceed with schedule it  "

    msg = EmailMessage() 
    msg['Subject'] = 'Greetings From Drivekraft!!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = reciever

    msg.set_content(msg1 + msg2  + msg3)

    #msg.add_alternative(content(), subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("hiii")


    return    

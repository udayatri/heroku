from flask import Flask
from datetime import datetime
import requests
import os
import smtplib
import imghdr
import json
import time
from helo import whattsappTakeover,firstMsg,intialGreetingProcess


app = Flask(__name__) #create a flask object

@app.route('/')
def index():
  intialGreetingProcess()
  whattsappTakeover()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  firstMsg("Dipesh","918284990439",current_time)
  firstMsg("Uday","919138439446",current_time )
  firstMsg("Deepanshu","919821084763",current_time )
  firstMsg("Rahul","917579469285",current_time )
  return "helo world"



# def hello():
#   # -- coding: utf-8 --
#   """
#   Created on Fri Nov 12 22:15:54 2021

#   @author: hp
#   """








#   def whattsappTakeover():



#       #configurations need to read from configurations.yaml file
#       # with open("spreadsheetFunctions/configurations.yaml", "r") as ymlfile:
#       #     cfg = yaml.load(ymlfile)

#       #reading instance id   
#       instanceid="instance294124"

#       url = "https://api.chat-api.com/"+ str(instanceid)+ "/takeover?token=bfllgpii7xqb42zq"

#       payload={}
#       headers = {}

#       response = requests.request("GET", url, headers=headers, data=payload)

#       if str(json.loads(response.text)['result'])=='Takeover request sent to WhatsApp':
#           print("Instance takingover taking place , will take around 4-5 seconds")
#           time.sleep(5)
      
#       print("Whattsapp instance is activated")

#       return 




#   def firstMsg(name,number,number1):
#       url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"

#       payload="{\r\n  \"body\": \"Hi " + str(name.title()) + " " + str(number1) +"\\n its working\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
#       headers = {
#               'Content-Type': 'application/json'
#               }

#       response = requests.request("POST", url, headers=headers, data=payload)

#       print(response.text)
#       return



#   whattsappTakeover()

#   now = datetime.now()

#   current_time = now.strftime("%H:%M:%S")
#   # firstMsg("Dipesh","918284990439",current_time)
#   # firstMsg("Uday","919138439446",current_time )
#   # firstMsg("Deepanshu","919821084763",current_time )
#   # firstMsg("Rahul","917579469285",current_time )
  

if __name__ == '__main__':
    app.run(debug= False ) #debug enabled is creating warning and error
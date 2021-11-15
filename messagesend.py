# from flask import Flask
# from datetime import datetime
# import requests
# import os
# import smtplib
# import imghdr
# import json
# import time
# import yaml
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import pandas as pd
# from email.message import EmailMessage

  


# def updateCells(spreadsheet,row,col, val):
    
#     if val=='':
#         return
    
#     print(val)
    
#     spreadsheet.update_cell(row , col , val)
#     time.sleep(1)
#     return 




# def whattsappTakeover():



#     #configurations need to read from configurations.yaml file
#     # with open("spreadsheetFunctions/configurations.yaml", "r") as ymlfile:
#     #     cfg = yaml.load(ymlfile)

#     #reading instance id   
#     instanceid="instance294124"

#     url = "https://api.chat-api.com/"+ str(instanceid)+ "/takeover?token=bfllgpii7xqb42zq"

#     payload={}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload)

#     if str(json.loads(response.text)['result'])=='Takeover request sent to WhatsApp':
#         print("Instance takingover taking place , will take around 4-5 seconds")
#         time.sleep(5)
    
#     print("Whattsapp instance is activated")

#     return 




# def firstMsg1(name,number,number1):
#     url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"

#     payload="{\r\n  \"body\": \"Hi " + str(name.title()) + " " + str(number1) +"\\n its working\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
#     headers = {
#             'Content-Type': 'application/json'
#             }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)
#     return


# def firstMsg(name,number):
#     url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"

#     payload="{\r\n  \"body\": \"Hi " + str(name.title()) + "\\nYou registered for the interactive session with Drivekraft and here we are as promised \xF0\x9F\x98\x83 . \\n\\nIt's great that you are ready to talk and remember it's never too late.\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
#     headers = {
#             'Content-Type': 'application/json'
#             }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)
#     return
    

# def sendLink(name,number):
    
#     url = "https://api.chat-api.com/instance294124/sendLink?token=bfllgpii7xqb42zq"
    
#     payload="{\r\n  \"body\": \"https://forms.gle/dFdsNJMErDgeauWy5\",\r\n  \"previewBase64\": \"nn\",\r\n  \"title\": \"Follow up form\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
#     headers = {
#       'Content-Type': 'application/json'
#     }
    
#     response = requests.request("POST", url, headers=headers, data=payload)
    
#     print(response.text)
#     return


# def SecondMsg(name,number):
#     url = "https://api.chat-api.com/instance294124/sendMessage?token=bfllgpii7xqb42zq"
    
#     payload="{\r\n  \"body\": \"Can you please this above form\xF0\x9F\x98\x83 \\n\\nThis will help to know more about you and assign you the best match of psychologist \xF0\x9F\x98\x87 \xF0\x9F\x98\x87 \\n\\nDo let me know once you filled the form , I will proceed with schedule it\",\r\n  \"phone\": \"" +(number) + "\"\r\n}"
#     headers = {
#       'Content-Type': 'application/json'
#     }
    
#     response = requests.request("GET", url, headers=headers, data=payload)
    
#     print(response.text)
#     return



# def isNew(number,email):

#     scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#     creds =ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
#     client = gspread.authorize(creds)
#     spreadsheet = client.open("personal Dev").worksheet("Completed Session")
#     data = spreadsheet.get_all_values()
    
#     values=data[1:]
    
#     for entry in values:
#         if str(entry[2])==number or str(entry[3])==email:
#             return entry[5]


#     return True

# def isOnWhattsapp(number):

#     if str(number[0])=='+':
#         number = number[1:]
        
#     if len(number)==10:
#         number='91'+ str(number)


#     try: 
#         url = "https://api.chat-api.com/instance294124/checkPhone?token=bfllgpii7xqb42zq&phone=" + str(number) 
    
#         payload={}
#         headers = {}
        
#         response = requests.request("GET", url, headers=headers, data=payload)
        
        
#         json_data = json.loads(response.text)['result']
        
#         if json_data=='not exists':
#             return False
    
    
#         return True    
        
#     except:
#         return False



# def send_Message(name,number):
    
#     if str(number[0])=='+':
#         number = number[1:]
        
#     if len(number)==10:
#         number='91'+ str(number)

#     if isOnWhattsapp(number)==False:
#         return False
        
#     firstMsg(name,number)
#     sendLink(name,number)
#     SecondMsg(name,number)
     
#     return
        
        

# def send_mail(name,reciever):

#     EMAIL_ADDRESS = "drivekraft@gmail.com"
#     EMAIL_PASSWORD = 'kxgudynwonausuqh'
    
#     msg1="Hi " + str(name)+" \nYou registered for the interactive session with Drivekraft and here we are as promised 😃 .  \nIt's great that you are ready to talk and remember it's never too late."
    
#     msg2="\n\n https://forms.gle/dFdsNJMErDgeauWy5"
    
#     msg3="\n\nCan you please this above form😃  \nThis will help to know more about you and assign you the best match of psychologist 😇 😇  \n\nDo let us know once you filled the form , I will proceed with schedule it  "

#     msg = EmailMessage() 
#     msg['Subject'] = 'Greetings From Drivekraft!!'
#     msg['From'] = EMAIL_ADDRESS
#     msg['To'] = reciever

#     msg.set_content(msg1 + msg2  + msg3)

#     #msg.add_alternative(content(), subtype='html')


#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         smtp.send_message(msg)
#         print("hiii")


#     return    




# def intialGreetingProcess():

#     #confihurations need to read from configurations.yaml file
#     with open("configurations.yaml", "r") as ymlfile:
#         cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)


#     #last index till GF1 was read    
#     gf1LastReadIndex=cfg["gf1LastReadIndex"]
    

#     #reading spreadsheet
#     scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#     creds =ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
#     client = gspread.authorize(creds)

#     #reading data from Google form 1 
#     gf1Spreadsheet = client.open("Dev Session Record CRM version").worksheet("GF1")
#     gf1Data = gf1Spreadsheet.get_all_values()
#     gf1RemainingData=gf1Data[gf1LastReadIndex:]
#     print(gf1RemainingData)
     

#     #reading data from stage 1 
#     st1Spreadsheet = client.open("Dev Session Record CRM version").worksheet("Stage 1")
#     st1Data = st1Spreadsheet.get_all_values()
#     st1DataCurrentLength=len(st1Data)


#     #reading  stage 2 data
#     st2Spreadsheet = client.open("Dev Session Record CRM version").worksheet("Stage 2")
#     st2Data = st2Spreadsheet.get_all_values()
#     st2DataCurrentLength=len(st2Data)


#     #moving data from gf1 to st1 or st2
#     for entry in gf1RemainingData:

#         timeStamp=entry[0]
#         name= entry[1]
#         number= entry[2]
#         email=entry[3]
#         country=entry[4]


#         psychologistName=isNew(number,email)

#         newComer=''

#         if(str(psychologistName)=='True'):

#             if (isOnWhattsapp(number)): # to check if person is avaible on whattsapp
#                 send_Message(name,number) 
#                 print("message send")
#                 status="msg send"
#             else:
#                  send_mail(name,email) #to send mail if he is not on whattsapp
#                  print("mail  send") 
#                  status="email send"  
#             newComer='Yes'

#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,1, timeStamp)
#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,2, name)
#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,3, number)
#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,4, email)
#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,5, country)
#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,7, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
#             updateCells(st1Spreadsheet,st1DataCurrentLength+1,6, status)        
    
#             st1DataCurrentLength=st1DataCurrentLength+1
            
#         else:
#             updateCells(st2Spreadsheet,st2DataCurrentLength+1,1, timeStamp)
#             updateCells(st2Spreadsheet,st2DataCurrentLength+1,2, name)
#             updateCells(st2Spreadsheet,st2DataCurrentLength+1,3, number)
#             updateCells(st2Spreadsheet,st2DataCurrentLength+1,4, email)
#             updateCells(st2Spreadsheet,st2DataCurrentLength+1,5, country)
#             updateCells(st2Spreadsheet,st2DataCurrentLength+1,9, psychologistName)

#             st2DataCurrentLength= st2DataCurrentLength+1

        
#         gf1LastReadIndex=gf1LastReadIndex+1
        
        
#     #updating last read in configuration file              
#     cfg["gf1LastReadIndex"]= gf1LastReadIndex
#     with open('configurations.yaml', 'w') as fp:
#         yaml.dump(cfg, fp)

#     return    




#whattsappTakeover()

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# firstMsg("Dipesh","918284990439",current_time)
# firstMsg("Uday","919138439446",current_time )
# firstMsg("Deepanshu","919821084763",current_time )
# firstMsg("Rahul","917579469285",current_time )
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






def updateCells(spreadsheet,row,col, val):
    
    if val=='':
        return
    
    print(val)
    
    spreadsheet.update_cell(row , col , val)
    time.sleep(1)
    return 

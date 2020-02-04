import json
import requests
import time
import winsound
#from tkinter import messagebox
from pymsgbox import *
import sys

def alert_msg(info, msg):
    #time.sleep(10)
    #messagebox.showinfo(info, msg)
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    alert(text=msg, title=info, button='OK')
    
def function(url):
    while True:
      try:
        data = requests.get(url)
        data = data.text
        time.sleep(180)
        data1 = requests.get(url)
        data1 = data1.text
      except Exception as e:
          alert_msg("ERROR", "RUN SCRIPT AGAIN")
          print("Exception ..............................................")
          time.sleep(500)
          function()
      if data != data1 :
          winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
          alert_msg("HURRY", "CHECK FOR TICKETS")
          time.sleep(100)

#alert_msg("test","TEST")
try:
    url = sys.argv[1]
except IndexError:
    print("Please provide a url")
    sys.exit(1)
function(url)

import random
import requests
from colorama import Fore, init

token = 'TOKEN-HERE'

#  Choose one of them
# invisible
# dnd
# online

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
status = {
    'status': "online"
  }

while True:
    try:
        request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=status)
        print('Forcing status: '+Fore.GREEN+status['status']+Fore.RESET)
    except:
        print('Error')
# Thanks to H4XOR#1337 for helping ;)

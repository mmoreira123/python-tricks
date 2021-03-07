#!/usr/bin/python
import requests
import time
import sys

url = sys.argv[1]

status = True
while status:
    response = requests.get(url)
    if (response.status_code == 200):
        print("status code is 200, hence exiting")
        status = False
    elif (response.status_code != 200):
        print("Status code is not 200, waiting unitl is up and running")
        time.sleep(5)

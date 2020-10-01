#!/usr/bin/env python3
import requests
import os,glob

# url : -.-.-.-./ 
url = ""
path = "supplier-data/images"
for f in os.listdir(path):
    with open("supplier-data/images/{}".format(f),"rb") as opened:
        r = requests.post(url, files={'file': opened})
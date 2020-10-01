#!/usr/bin/env python3
import os
import requests

for file in os.listdir("supplier-data/descriptions/"):
    with open("supplier-data/descriptions/{}".format(file),"r") as f:
        data = f.read()
        data = data.split('\n')
        image_name = file.strip(".txt") + ".jpeg"
        dic = {"name":data[0], "weight":int(data[1].strip(" lbs")), "description":data[2], "image_name":image_name}
        response = requests.post('http://http://.your ip.../fruits', json=dic)

#!/usr/bin/env python3
import os
from datetime import date 
import reports
import requests
import emails

paragraph = ""
today = date.today().strftime("%B %d, %Y")
title = "Processed Update on <Today's date>".format(today)

for file in os.listdir("supplier-data/descriptions/"):
    with open("supplier-data/descriptions/{}".format(file),"r") as f:
        data = f.read()
        data = data.split('\n')
        name = "name: " + data[0]
        weight = "weight: "+data[1]
        paragraph += name + "<br/>" + weight + "<br/><br/>"


    
if __name__ == "__main__":
    reports.generate_report('/tmp/processed.pdf', title, paragraph)
    #2nd trial only #################################################################
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
    

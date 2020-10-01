#!/usr/bin/env python3
import psutil
import emails
import socket
import os

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

# a stupid way just in case too many errors at the same time
cpu = psutil.cpu_percent()
if cpu > 80 :
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)

mem = psutil.virtual_memory()
THRESHOLD = 500 * 1024 * 1024  
if mem.available < THRESHOLD:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)

### faculty student ?? 
disk = psutil.disk_usage('/') 
if disk.percent > 80:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)

host_ip = socket.gethostbyname('localhost')
if host_ip != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender,receiver,subject,body)
    emails.send_email(message)

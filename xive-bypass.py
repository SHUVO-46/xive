import random,os,time,requests
import os

file_path = "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py"

# GitHub থেকে লাইভ লাইসেন্স নেওয়ার কোড
replacement_code = '''
try:
    import requests
    content = requests.get("https://raw.githubusercontent.com/SHUVO-46/CONTROL-ROOM/main/Approval.txt").text.strip()
except:
    content = "LICENSE_FETCH_ERROR"
'''

# models.py ফাইল পড়া
with open(file_path, 'r') as file:
    lines = file.readlines()

# পুরনো content = str(...) লাইন খোঁজা ও বদলানো
with open(file_path, 'w') as file:
    for line in lines:
        if "content = str(" in line:
            file.write(replacement_code + "\n")
        else:
            file.write(line)
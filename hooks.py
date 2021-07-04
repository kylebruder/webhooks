#!/usr/bin/python3

import requests
import json

# Hooks. Enter hook urls here
hooks = []


# Bitcoin price index via Coindesk

bpi = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
date = bpi['time']['updated']
disclaimer = bpi['disclaimer']
price = bpi['bpi']['USD']['rate']

content = """
As of {}, the USD market value of Bitcoin was ${}.\n
Disclaimer:
{}
""".format(date, price, disclaimer)

# Build message
message = {
        'content': content,
        }
# Check to make sure the content will fit
if len(message['content']) <= 2000:
    for h in hooks:
        r = requests.post(h, json=message)
        #print(h)
        #print(content)    
else:
    raise Exception("Content is too long! Must be less than 2000 characters")
#print(r.status_code)

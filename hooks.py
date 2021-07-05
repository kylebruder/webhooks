#!/usr/bin/python3

import requests
import json
from datetime import datetime

# Hooks
hooks = []

# Number of spams
n = 100

def generate_timestamp_message():
    '''
    Returns a json message with a timestamp.
    For testing purposes.
    '''
    time = datetime.now()
    content = """
    generated on roadsauce at {}
    """.format(time)

    # Build message
    message = {
        'content': content,
    }
    return message

# Check to make sure the content will fit
for h in hooks:
    for x in range(n):
        message = generate_timestamp_message()
        if len(message['content']) <= 2000:
            r = requests.post(h, json=message)
            #print(h)
            #print(content)    
            print("response code: {} - response time (seconds): {}".format(
                r.status_code,
                r.elapsed.total_seconds()
            ))
        else:
            raise Exception("Content is too long! Must be less than 2000 characters")

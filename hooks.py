#!/usr/bin/python3

import requests
import json
import time
from datetime import datetime

# Hooks
hooks = []

# Number of spams
n = 100

# Delay between messages in seconds
delay = 0 

def generate_timestamp_message(delay=0):
    '''
    Returns a json message with a timestamp.
    For testing purposes.
    '''
    time = datetime.now()
    content = """
    generated on roadsauce at {} - delay after POST (seconds): {}
    """.format(time, delay)

    # Build message
    message = {
        'content': content,
    }
    return message

# Check to make sure the content will fit
def spam_hooks(delay=0):
    for h in hooks:
        for x in range(n):
            message = generate_timestamp_message(delay=delay)
            if len(message['content']) <= 2000:
                r = requests.post(h, json=message)
                time.sleep(delay)
                #print(h)
                #print(content)    
                print("{} - response code: {} - response time (seconds): {}".format(
                    x,
                    r.status_code,
                    r.elapsed.total_seconds()
                ))
            else:
                raise Exception("Content is too long! Must be less than 2000 characters")


def main():
    spam_hooks(delay=delay)

if __name__ == "__main__":
    main()

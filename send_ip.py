import requests
import json
from datetime import datetime
import time
from subprocess import check_output
import socket

if __name__ == '__main__':

    # This header sets the HTTP request's mimetype to `application/json`. This
    # means the payload of the HTTP message will be formatted as a json ojbect
    hdr = {
        'Content-Type': 'application/json',
        'Authorization': None #not using HTTP secure
    }

    hostname = socket.gethostname()
    info = check_output('ifconfig | grep wlan0 -A1 | grep inet', shell=True).strip()
    # The payload of our message starts as a simple dictionary. Before sending
    # the HTTP message, we will format this into a json object
    payload = {
        'time': str(datetime.now()),
        'hostname': hostname,
        'network': info
    }

    for i in range(2):
        # Send an HTTP POST message and block until a response is given.
        # Note: requests() is NOT the same thing as request() under the flask 
        # library.
        response = requests.post("http://eclipse.usc.edu:10510/post-event", headers = hdr,
                                 data = json.dumps(payload))

        # Print the json object from the HTTP response
        print(response.json())

        time.sleep(2)

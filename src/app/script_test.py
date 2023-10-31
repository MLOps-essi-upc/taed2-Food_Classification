"""
Module Name: script_test.py

Script for accessing the API programmatically
"""

import json
import requests

# Set a timeout (in seconds) for the HTTP request
TIMEOUT = 10  # You can adjust the value as needed

response = requests.get("http://10.4.41.33:5000/", timeout=TIMEOUT)
print(json.loads(response.text))

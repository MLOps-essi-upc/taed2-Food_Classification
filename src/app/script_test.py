"""Script for accessing the API programmatically"""

import json
import requests

response = requests.get("http://10.4.41.33:5000/")
print(json.loads(response.text))
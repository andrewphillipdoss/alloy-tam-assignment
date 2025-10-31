import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

token = os.getenv("ALLOY_WORKFLOW_TOKEN")
secret = os.getenv("ALLOY_WORKFLOW_SECRET")

url = "https://sandbox.alloy.co/v1/parameters/"

try:
    response = requests.get(
        url,
        auth=(token, secret),
        headers={"Accept": "application/json"},
        timeout=20
    )

    print("Status code:", response.status_code)
    response.raise_for_status()  # raise error for non-200s

    data = response.json()

    # Pretty-print the full response
    print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print("HTTP Request failed:", e)
except Exception as e:
    print("Unexpected error:", e)

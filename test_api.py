import requests
import json

student = {
    "placementtraining": 1,  # Changed from "yes" to 1
    "extracurricularactivities": 1,  # Changed from "yes" to 1
    "aptitudetestscore": 85,
    "hsc_marks": 75,
    "softskillsrating": 4
}

url = "http://localhost:2525/predict"
response = requests.post(url, json=student)

try:
    result = response.json()
    print(json.dumps(result, indent=2))
except requests.exceptions.JSONDecodeError:
    print("Error: Could not decode JSON response. Check if the API is running correctly.")

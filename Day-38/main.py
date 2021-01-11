import requests
import os
from datetime import datetime

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
APP_ID = os.environ.get("NT_APP_ID")
API_KEY = os.environ.get("NT_API_KEY")
TOKEN = os.environ.get("TOKEN")

exercise_text = input("Tell me which exercises you did: ")

GENDER = "male"
WEIGHT_KG = 55.7
HEIGHT_CM = 172.6
AGE = 24

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, headers=headers, json=exercise_config)
result = response.json()

exercise_data = result["exercises"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_header = {
    "Authorization": f"Basic {TOKEN}"
}
# headers.append("Authorization", "Basic bnVsbDpudWxs")

for exercise_data in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise_data["name"].title(),
            "duration": exercise_data["duration_min"],
            "calories": exercise_data["nf_calories"],
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_header)
    print(response.text)

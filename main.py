import os
import requests
from datetime import datetime

APP_ID = os.getenv("APP_ID")
APP_API_KEY=os.getenv("APP_API_KEY")
print(APP_ID)
Weight=70
Height=171
Age=21
Gender="male"
print(APP_ID,APP_API_KEY)



headers={
"x-app-id": APP_ID,
"x-app-key":APP_API_KEY
}
# print(headers["x-app-id"])


exercise_text=input("Tell me which exercises you did today:")

check_url=os.environ.get("NUTRITION_URL","URL is invalid")
check_params={
    "query":exercise_text,
    "weight_kg": Weight,
    "height_cm":Height,
    "age":Age,
    "gender":Gender
}
# print(check_url)
response=requests.post(url=check_url,json=check_params,headers=headers)
result=response.json()
print(result)

sheety_url=os.environ["SHEETY_URL"]
print(sheety_url)

today=datetime.now().strftime("%d/%m/%Y")
time=datetime.now().strftime("%X")

sheety_headers={
"Authorization": os.environ.get("SHEETY_AUTHORIZATION")
}
print(sheety_headers["Authorization"])


for exercise in result["exercises"]:
    sheety_params={
        "workout":{
            "date":today,
            "time": time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_url, json=sheety_params,headers=sheety_headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)




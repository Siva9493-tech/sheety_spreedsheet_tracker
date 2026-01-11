import requests
from datetime import datetime
# Your personal data. Used by the Exercise & Nutrition API to calculate calories.
Weight=70
Height=171
Age=21
Gender="male"

# Nutrition APP ID and API Key. Actual values are stored as environment variables.
APP_ID = "app_9f49e60012934749937f2cf8"
API_KEY = "nix_live_QNf5kqCUHH3d314M5gLBPge5gJn4GfKh"
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

check_params={
    "query":exercise_text,
    "weight_kg": Weight,
    "height_cm":Height,
    "age":Age,
    "gender":Gender
}

response = requests.post(url=exercise_endpoint, json=check_params, headers=headers)
result = response.json()
print(result)
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint

sheet_endpoint ="https://api.sheety.co/a78096d0139ece359ac94825a0d0e413/workouts/workouts"


# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    bearer_headers = {
        "Authorization":"Bearer qwertyuiopasdfghjklzxcvbnm"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(f"Sheety Response: \n {sheet_response.text}")
    #
    # # Sheety Authentication Option 1: No Auth
    # """
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    # """
    #
    # # Sheety Authentication Option 2: Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["ENV_SHEETY_USERNAME"],
    #         os.environ["ENV_SHEETY_PASSWORD"],
    #     )
    # )
    #
    # # Sheety Authentication Option 3: Bearer Token
    # """
    # bearer_headers = {
    #     "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )
    # """
    # print(f"Sheety Response: \n {sheet_response.text}")

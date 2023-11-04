from auth import *
import requests
from datetime import date
from datetime import datetime as dt

url_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")
params_nutritionix = {
        "query": query,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": age,
        }

headers_nutritionix = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        }
exercises = requests.post(url=url_exercise,
                          json=params_nutritionix,
                          headers=headers_nutritionix).json()
#print(response.json())

url_sheety = f"https://api.sheety.co/{USER}/{PROJECT}/{SHEET}s"

headers_sheety = {
        "Authorization": f"Bearer {TOKEN}",
        }

for row in exercises["exercises"]:
    params_sheety = {
            SHEET: {
                "date": date.today().strftime("%d/%m/%Y"),
                "time": dt.now().strftime("%X"),
                "exercise": row["name"].title(),
                "duration": row["duration_min"],
                "calories": row["nf_calories"],
                }
            }

    response = requests.post(url=url_sheety,
                             json=params_sheety,
                             headers=headers_sheety)
    print(response.json())

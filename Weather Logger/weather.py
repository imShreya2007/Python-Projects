import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

print("Weather Logger (API + CSV)...")

FILENAME = "weather_log.csv"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    print("Error: OPENWEATHER_API_KEY not set.")
    exit(1)


# Create CSV if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Time", "City", "Temperature (°C)", "Weather"])

def log_weather():
    city = input("Enter city name: ").strip().title()

    if not city:
        print("City name cannot be empty.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    # Check if already logged today
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print(f"Weather for {city} already logged today.")
                return

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
        "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 404:
            print("City not found.")
            return
        elif response.status_code != 200:
            print("API error. Try again later.")
            return


        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        time = datetime.now().strftime("%H:%M:%S")

        with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, time, city, temperature, description])

        print(f"Weather logged for {city} on {date} ({temperature}°C, {description})")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    while True:
        log_weather()
        choice = input("Log another city? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting Weather Logger.")
            break

if __name__ == "__main__":
    main()


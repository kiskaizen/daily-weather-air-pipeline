import requests
import csv
from datetime import date
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
aq_api_key = os.getenv("AQ_API_KEY")

cities = ["Greater Noida", "Delhi", "Mumbai", "Bangalore"]

for city in cities:
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        today = date.today()
        print(f"{city} -> Temperature: {temperature}, Description: {description}")
    except Exception as e:
        print(f"Something went wrong while fetching weather data for {city}:", e)
        continue

    try:
        with open("weather_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([today, city, temperature, description])
        print(f"Saved {city} weather!")
    except Exception as e:
        print(f"Something went wrong while saving {city} to CSV:", e)

    try:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA")
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather_log (log_date, city, temperature, description) VALUES (%s, %s, %s, %s)",
            (today, city, temperature, description)
        )
        cursor.close()
        conn.close()
        print(f"Saved {city} to Snowflake too!")
    except Exception as e:
        print(f"Something went wrong while saving {city} to Snowflake:", e)

aq_stations = {
    "Sector - 125, Noida": 12235187,
    "R K Puram, Delhi": 35,
    "Kurla, Mumbai": 19978,
    "Jayanagar 5th Block, Bengaluru": 12235267
}

for station_name, sensor_id in aq_stations.items():
    try:
        headers = {"X-API-Key": aq_api_key}
        measurement_url = f"https://api.openaq.org/v3/sensors/{sensor_id}/measurements?limit=1"
        aq_response = requests.get(measurement_url, headers=headers)
        aq_data = aq_response.json()
        pm25_value = aq_data["results"][0]["value"]
        print(f"{station_name} -> PM2.5: {pm25_value}")
    except Exception as e:
        print(f"Something went wrong while fetching air quality data for {station_name}:", e)
        continue

    try:
        with open("air_quality_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date.today(), station_name, pm25_value])
        print(f"Saved {station_name} air quality to CSV!")
    except Exception as e:
        print(f"Something went wrong while saving {station_name} to CSV:", e)

    try:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA")
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO air_quality_log (log_date, station_name, pm25) VALUES (%s, %s, %s)",
            (date.today(), station_name, pm25_value)
        )
        cursor.close()
        conn.close()
        print(f"Saved {station_name} to Snowflake too!")
    except Exception as e:
        print(f"Something went wrong while saving {station_name} to Snowflake:", e)
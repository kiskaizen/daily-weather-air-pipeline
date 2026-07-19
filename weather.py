#import requests

#api_key = ""
#city = "Greater Noida"

#url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#response = requests.get(url)
#data = response.json()

#temperature = data["main"]["temp"]
#description = data["weather"][0]["description"]

#print("Temperature:", temperature)
#print("Description:", description)




#import csv
#from datetime import date

#today = date.today()

#with open("weather_log.csv", "a", newline="") as file:
#    writer = csv.writer(file)
#    writer.writerow([today, city, temperature, description])

#print("Saved today's weather!")



#import snowflake.connector

#conn = snowflake.connector.connect(
#    user="",
#    password="",
#    account="",
#    warehouse="",
#    database="",
#   schema=""
#)

#cursor = conn.cursor()

#cursor.execute(
#   "INSERT INTO weather_log (log_date, city, temperature, description) VALUES (%s, %s, %s, %s)",
#    (today, city, temperature, description)
#)

#cursor.close()
#conn.close()

#print("Saved to Snowflake too!")



from dotenv import load_dotenv
import os

load_dotenv()


import requests
import csv
from datetime import date
import snowflake.connector


api_key = os.getenv("WEATHER_API_KEY")
city = "Greater Noida"

try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    today = date.today()

    print("Temperature:", temperature)
    print("Description:", description)

except Exception as e:
    print("Something went wrong while fetching weather data:", e)
    exit()  # stop here, no point continuing if we have no data

try:
    with open("weather_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, city, temperature, description])
    print("Saved today's weather!")

except Exception as e:
    print("Something went wrong while saving to the CSV file:", e)

try:
    conn = snowflake.connector.connect(
        #user="",
	user=os.getenv("SNOWFLAKE_USER"),
        #password="",
	password=os.getenv("SNOWFLAKE_PASSWORD"),
        #account="",
	account=os.getenv("SNOWFLAKE_ACCOUNT"),
        #warehouse="",
	warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        #database="",
	database=os.getenv("SNOWFLAKE_DATABASE"),
        #schema=""
	schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather_log (log_date, city, temperature, description) VALUES (%s, %s, %s, %s)",
        (today, city, temperature, description)
    )
    cursor.close()
    conn.close()
    print("Saved to Snowflake too!")

except Exception as e:
    print("Something went wrong while saving to Snowflake:", e)





#try:
    #aq_api_key = ""
    #headers = {"X-API-Key": aq_api_key}

    #locations_url = "https://api.openaq.org/v3/locations?coordinates=28.4744,77.5040&radius=25000&limit=1"
    #locations_url = "https://api.openaq.org/v3/locations?coordinates=28.4744,77.5040&radius=50000&limit=10"
    #locations_url = "https://api.openaq.org/v3/locations?coordinates=28.4744,77.5040&radius=25000&limit=10"	
    #loc_response = requests.get(locations_url, headers=headers)
    #loc_data = loc_response.json()

    #print(loc_data)

#except Exception as e:
    #print("Something went wrong while fetching air quality location:", e)



try:
    #aq_api_key = ""
    aq_api_key = os.getenv("AQ_API_KEY")    
    headers = {"X-API-Key": aq_api_key}

    pm25_sensor_id = 12235187
    measurement_url = f"https://api.openaq.org/v3/sensors/{pm25_sensor_id}/measurements?limit=1"
    aq_response = requests.get(measurement_url, headers=headers)
    aq_data = aq_response.json()

    pm25_value = aq_data["results"][0]["value"]
    print("PM2.5:", pm25_value)

except Exception as e:
    print("Something went wrong while fetching air quality data:", e)



try:
    with open("air_quality_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, "Sector - 125, Noida", pm25_value])
    print("Saved air quality to CSV!")

except Exception as e:
    print("Something went wrong while saving air quality to CSV:", e)

try:
    conn = snowflake.connector.connect(
        #user="",
	user=os.getenv("SNOWFLAKE_USER"),
        #password="",
	password=os.getenv("SNOWFLAKE_PASSWORD"),
        #account="",
	account=os.getenv("SNOWFLAKE_ACCOUNT"),
        #warehouse="",
	warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        #database="",
	database=os.getenv("SNOWFLAKE_DATABASE"),
        #schema=""
	schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO air_quality_log (log_date, station_name, pm25) VALUES (%s, %s, %s)",
        (today, "Sector - 125, Noida", pm25_value)
    )
    cursor.close()
    conn.close()
    print("Saved air quality to Snowflake too!")

except Exception as e:
    print("Something went wrong while saving air quality to Snowflake:", e)
#import streamlit as st
#import pandas as pd

#st.title("My Weather & Air Quality Dashboard")

#st.write("Hello! This is my dashboard.")



#import streamlit as st
#import pandas as pd

#st.title("Weather & Air Quality Dashboard")

#weather_data = pd.read_csv("weather_log.csv", header=None,
#    names=["date", "city", "temperature", "description"])

#st.subheader("Weather Data")
#st.dataframe(weather_data)




#st.subheader("Temperature Over Time")
#st.line_chart(weather_data, x="date", y="temperature")




#aq_data = pd.read_csv("air_quality_log.csv", header=None,
#    names=["date", "station", "pm25"])

#st.subheader("Air Quality Data")
#st.dataframe(aq_data)

#st.subheader("PM2.5 Over Time")
#st.line_chart(aq_data, x="date", y="pm25")

#------------------------------------------------


#import streamlit as st
#import pandas as pd
#import snowflake.connector
#import os
#from dotenv import load_dotenv

#load_dotenv()

#st.title("My Weather & Air Quality Dashboard")

#conn = snowflake.connector.connect(
#    user=os.getenv("SNOWFLAKE_USER"),
#    password=os.getenv("SNOWFLAKE_PASSWORD"),
#    account=os.getenv("SNOWFLAKE_ACCOUNT"),
#    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
#    database=os.getenv("SNOWFLAKE_DATABASE"),
#    schema=os.getenv("SNOWFLAKE_SCHEMA")
#)

#def get_secret(key):
#    if key in st.secrets:
#        return st.secrets[key]
#    return os.getenv(key)

#conn = snowflake.connector.connect(
#    user=get_secret("SNOWFLAKE_USER"),
#    password=get_secret("SNOWFLAKE_PASSWORD"),
#    account=get_secret("SNOWFLAKE_ACCOUNT"),
#    warehouse=get_secret("SNOWFLAKE_WAREHOUSE"),
#    database=get_secret("SNOWFLAKE_DATABASE"),
#    schema=get_secret("SNOWFLAKE_SCHEMA")
#)

#weather_data = pd.read_sql("SELECT * FROM weather_log ORDER BY log_date", conn)
#aq_data = pd.read_sql("SELECT * FROM air_quality_log ORDER BY log_date", conn)

#conn.close()

#st.subheader("Weather Data")
#st.dataframe(weather_data)

#st.subheader("Temperature Over Time")
#st.line_chart(weather_data, x="LOG_DATE", y="TEMPERATURE")

#st.subheader("Air Quality Data")
#st.dataframe(aq_data)

#st.subheader("PM2.5 Over Time")
#st.line_chart(aq_data, x="LOG_DATE", y="PM25")



#----------------------------------------------------------



import streamlit as st
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

st.title("My Weather & Air Quality Dashboard")

#def get_secret(key):
#    if key in st.secrets:
#        return st.secrets[key]
#    return os.getenv(key)

def get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key)

conn = snowflake.connector.connect(
    user=get_secret("SNOWFLAKE_USER"),
    password=get_secret("SNOWFLAKE_PASSWORD"),
    account=get_secret("SNOWFLAKE_ACCOUNT"),
    warehouse=get_secret("SNOWFLAKE_WAREHOUSE"),
    database=get_secret("SNOWFLAKE_DATABASE"),
    schema=get_secret("SNOWFLAKE_SCHEMA")
)

weather_data = pd.read_sql("SELECT * FROM weather_log ORDER BY log_date", conn)
aq_data = pd.read_sql("SELECT * FROM air_quality_log ORDER BY log_date", conn)

conn.close()

city_list = weather_data["CITY"].unique()
selected_city = st.selectbox("Choose a city", city_list)

filtered_weather = weather_data[weather_data["CITY"] == selected_city]

st.subheader(f"Weather Data — {selected_city}")
st.dataframe(filtered_weather)

st.subheader(f"Temperature Over Time — {selected_city}")
st.line_chart(filtered_weather, x="LOG_DATE", y="TEMPERATURE")

station_list = aq_data["STATION_NAME"].unique()
selected_station = st.selectbox("Choose an air quality station", station_list)

filtered_aq = aq_data[aq_data["STATION_NAME"] == selected_station]

st.subheader(f"Air Quality Data — {selected_station}")
st.dataframe(filtered_aq)

st.subheader(f"PM2.5 Over Time — {selected_station}")
st.line_chart(filtered_aq, x="LOG_DATE", y="PM25")


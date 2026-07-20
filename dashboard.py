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




import streamlit as st
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

st.title("My Weather & Air Quality Dashboard")

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

weather_data = pd.read_sql("SELECT * FROM weather_log ORDER BY log_date", conn)
aq_data = pd.read_sql("SELECT * FROM air_quality_log ORDER BY log_date", conn)

conn.close()

st.subheader("Weather Data")
st.dataframe(weather_data)

st.subheader("Temperature Over Time")
st.line_chart(weather_data, x="LOG_DATE", y="TEMPERATURE")

st.subheader("Air Quality Data")
st.dataframe(aq_data)

st.subheader("PM2.5 Over Time")
st.line_chart(aq_data, x="LOG_DATE", y="PM25")
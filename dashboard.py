#import streamlit as st
#import pandas as pd

#st.title("My Weather & Air Quality Dashboard")

#st.write("Hello! This is my dashboard.")



import streamlit as st
import pandas as pd

st.title("Weather & Air Quality Dashboard")

weather_data = pd.read_csv("weather_log.csv", header=None,
    names=["date", "city", "temperature", "description"])

st.subheader("Weather Data")
st.dataframe(weather_data)




st.subheader("Temperature Over Time")
st.line_chart(weather_data, x="date", y="temperature")




aq_data = pd.read_csv("air_quality_log.csv", header=None,
    names=["date", "station", "pm25"])

st.subheader("Air Quality Data")
st.dataframe(aq_data)

st.subheader("PM2.5 Over Time")
st.line_chart(aq_data, x="date", y="pm25")
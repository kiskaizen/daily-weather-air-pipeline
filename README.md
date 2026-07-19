\# Daily Weather \& Air Quality Pipeline



A small automated data pipeline that fetches live weather and air quality data every day, stores it locally, and loads it into a Snowflake data warehouse.



\## What it does

\- Fetches current weather (temperature, conditions) for Greater Noida using the OpenWeatherMap API

\- Fetches live PM2.5 air quality readings from a nearby monitoring station using the OpenAQ API

\- Saves both datasets to local CSV files

\- Loads both datasets into Snowflake tables (`weather\_log`, `air\_quality\_log`)

\- Runs automatically every day using Windows Task Scheduler

\- Includes error handling so a failed API call or connection issue doesn't crash the whole pipeline



\## Tech used

\- Python (requests, csv, dotenv)

\- Snowflake (cloud data warehouse)

\- Windows Task Scheduler (automation)

\- Git \& GitHub (version control)



\## Why I built this

Built as a hands-on project to learn practical data engineering skills — API integration, cloud data warehousing, automation, and secure handling of credentials.



\## Setup

1\. Clone this repo

2\. Create a `.env` file with your own API keys and Snowflake credentials (see `.env` example below)

3\. Run `pip install -r requirements.txt`

4\. Run `python weather.py`



\### .env format

```

WEATHER\_API\_KEY=your\_key

AQ\_API\_KEY=your\_key

SNOWFLAKE\_USER=your\_username

SNOWFLAKE\_PASSWORD=your\_password

SNOWFLAKE\_ACCOUNT=your\_account

SNOWFLAKE\_WAREHOUSE=your\_warehouse

SNOWFLAKE\_DATABASE=your\_database

SNOWFLAKE\_SCHEMA=your\_schema

```


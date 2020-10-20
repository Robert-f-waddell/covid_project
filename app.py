import dash
import pandas as pd
covid_df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
covid_df = covid_df[["continent",
                     "location",
                     "date",
                     "total_cases",
                    "new_cases",
                    "new_cases_smoothed",
                    "total_deaths",
                    "new_deaths",
                    "new_deaths_smoothed",]]

covid_df = covid_df[covid_df["total_cases"].notna()]

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

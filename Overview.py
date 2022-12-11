import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display
from matplotlib import rcParams
import seaborn as sns
import plotly.express as px
import json
import requests
from streamlit_lottie import st_lottie
import streamlit_extras
from streamlit_extras.add_vertical_space import add_vertical_space

plt.style.use("ggplot")
rcParams["figure.figsize"] = (12, 6)

df = pd.read_csv('athlete_events.csv')
regions = pd.read_csv('noc_regions.csv')
df = df.merge(regions, on="NOC", how="left")
df.drop("notes", axis=1, inplace=True)


st.set_page_config(
    layout="centered",
    page_title="120 Years of Olympics",
    page_icon="🥇",
)
st.title("120 Years of Olympics")
st.sidebar.title("Navigation")

options = st.sidebar.radio(
    "Topics:",
    options=[
        "Data Frame Main Info",
        "Main Statisctics on Numbers",
        "Data Clean Up and Transformation",
    ],
)


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottiefile(
    "/Users/maximsukhoparov/PycharmProjects/Streamlit_App/68324-olympics-loader.json"
)
lottie_hello = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_iamb7tjt.json"
)


def separator(number=1):
    for i in range(number):
        st.write(" ")


if options == "Data Frame Main Info":
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.1, 2, 0.2, 2, 0.1))

    with row0_2:
        add_vertical_space()
    row0_1.subheader(
        "120 years of Olympic history: athletes and results [Kaggle]("
        "https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)"
    )
    row0_2.subheader(
        "A Streamlit web analytics app by [Tim Sukhoparov](https://github.com/tiwwpst)"
    )
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=300,
        width=500,
        key=None,
    )
    st.header("Data Set Main Info")
    st.subheader(
        "This is a historical dataset on the modern Olympic Games, including all the Games from Athens 1896 to "
        "Rio 2016."
    )
    st.subheader(
        "Note that the Winter and Summer Games were held in the same year up until 1992. After that, "
        "they staggered them such that Winter Games occur on a four year cycle starting with 1994, "
        "then Summer in 1996, then Winter in 1998, and so on. "
    )
    st.header("Dataframe")
    st.dataframe(df)
    separator(4)
    st.header("Content")
    st.subheader(
        "The file contains 271116 rows and 16 columns. Each row corresponds to an individual "
        "athlete competing in an individual Olympic event. The columns are:"
    )
    st.write("• ID - Unique number for each athlete")
    st.write("• Name - Athlete′s name")
    st.write("• Sex - M or F")
    st.write("• Age - Integer")
    st.write("• Height - In centimeters")
    st.write("• Weight - In kilograms")
    st.write("• Team - Team name")
    st.write("• NOC - National Olympic Committee 3-letter code")
    st.write("• Games - Year and season")
    st.write("• Year - Integer")
    st.write("• Season - Summer or Winter")
    st.write("• City - Host city")
    st.write("• Sport - Sport")
    st.write("• Event - Event")
    st.write("• Medal - Gold, Silver, Bronze, or NA")
    st.write("• Region - Participating Country")
    separator(4)
    st.header("NaN Analysis")
    a = 9474
    h = 60171
    w = 62875
    m = 231333
    col1, col2, col3, col4 = st.columns(4)
    col1.write(
        f"""<h3>Age Missing Values&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {a} </span></h3>""",
        unsafe_allow_html=True,
    )
    col2.write(
        f"""<h3>Height Missing Values&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {h} </span></h3>""",
        unsafe_allow_html=True,
    )
    col3.write(
        f"""<h3>Weight Missing Values&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:dodgerblue"> {w} </span></h3>""",
        unsafe_allow_html=True,
    )
    col4.write(
        f"""<h3>Medal Missing Values &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {m} </span></h3>""",
        unsafe_allow_html=True,
    )

if options == "Main Statisctics on Numbers":
    st.header("Main Statisctics on Numbers")
    st.write(df.describe(include="all"))
    separator(3)
    col1, col2, col3 = st.columns(3)
    col1.write(
        f"""<h3>Mean Age&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:dodgerblue"> {round(df.Age.mean(), 2)} </span></h3>""",
        unsafe_allow_html=True,
    )
    col2.write(
        f"""<h3>Median Age &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {df.Age.median()} </span></h3>""",
        unsafe_allow_html=True,
    )
    col3.write(
        f"""<h3>STD Age&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span 
        style="color:dodgerblue"> {round(df.Age.std(), 2)} </span></h3>""",
        unsafe_allow_html=True,
    )
    separator(4)
    col1, col2, col3 = st.columns(3)
    col1.write(
        f"""<h3>Mean Height&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:dodgerblue"> {round(df.Height.mean(), 2)} </span></h3>""",
        unsafe_allow_html=True,
    )
    col2.write(
        f"""<h3>Median Height &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {df.Height.median()} </span></h3>""",
        unsafe_allow_html=True,
    )
    col3.write(
        f"""<h3>STD Height &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {round(df.Height.std(), 2)} </span></h3>""",
        unsafe_allow_html=True,
    )
    separator(4)
    col1, col2, col3 = st.columns(3)
    col1.write(
        f"""<h3>Mean Weight &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {round(df.Weight.mean(), 2)} </span></h3>""",
        unsafe_allow_html=True,
    )
    col2.write(
        f"""<h3>Median Weight &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:dodgerblue"> {df.Weight.median()} </span></h3>""",
        unsafe_allow_html=True,
    )
    col3.write(
        f"""<h3>STD Weight&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:dodgerblue"> {round(df.Weight.std(), 2)} </span></h3>""",
        unsafe_allow_html=True,
    )


df[["Age", "Height", "Weight"]] = df[["Age", "Height", "Weight"]].fillna(
    df[["Age", "Height", "Weight"]].mean()
)
participants_with_medal = df[df["Medal"].notna()]
df["Medal"].fillna("No Medal", inplace=True)
summer_df = df[(df["Season"] == "Summer")]
winter_df = df[(df["Season"] == "Winter")]

summer_men_df = (
    summer_df[(summer_df["Sex"] == "M")].groupby("Year")["Name"].count().reset_index()
)
summer_women_df = (
    summer_df[(summer_df["Sex"] == "F")].groupby("Year")["Name"].count().reset_index()
)

summer_mw_df = summer_men_df.merge(summer_women_df, on="Year")
summer_mw_df.rename(columns={"Name_x": "Male", "Name_y": "Female"}, inplace=True)

winter_men_df = (
    winter_df[(winter_df["Sex"] == "M")].groupby("Year")["Name"].count().reset_index()
)
winter_women_df = (
    winter_df[(winter_df["Sex"] == "F")].groupby("Year")["Name"].count().reset_index()
)

winter_mw_df = winter_men_df.merge(winter_women_df, on="Year")
winter_mw_df.rename(columns={"Name_x": "Male", "Name_y": "Female"}, inplace=True)

if options == 'Data Clean Up and Transformation':
    st.header('Data Clean Up and Transformation')
    st.subheader('In the second file, where there is an explanation of the NOC, there is also a notes column that is '
                 'not necessary, so we can just delete it.')
    st.subheader(
        'From the NaN analysis, it is clear that there are many missing numbers, so I decided to replace NaN with the '
        'average of all the numbers in each column, respectively')
    lottie_coding = load_lottiefile(
        "/Users/maximsukhoparov/PycharmProjects/Streamlit_App/99797-data-management.json"
    )
    lottie_hello = load_lottieurl(
        "https://assets10.lottiefiles.com/packages/lf20_9wpyhdzo.json"
    )
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=300,
        width=500,
        key=None,
    )
    st.subheader(
        'Since most of the participants do not have a medal, I can make a new dataframe with only medalists.')
    st.subheader(
        'Also, I need to replace the NaNs in the "Medal" column with the value "No Medal".')
    st.subheader(
        'Then I need to split my dataframe into two parts. For the Summer Olympics and the Winter Olympics.')
    st.subheader(
        'For simplicity, I will immediately split each part into two more dataframes by gender.')
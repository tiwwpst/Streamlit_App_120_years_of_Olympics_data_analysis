import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display
from matplotlib import rcParams
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
from streamlit_lottie import st_lottie

from Overview import (
    summer_mw_df,
    winter_mw_df,
    summer_df,
    winter_df,
    df,
    participants_with_medal, load_lottiefile, load_lottieurl,
)

st.set_page_config(layout="centered")
st.title("Medals Info")
st.sidebar.title("Navigation")

options = st.sidebar.radio(
    "Topics:",
    options=[
        "Number of medals for each country",
        "Number of medals for each country for each sport",
        "All medals with descriptions of the year, country and sport",
        "The right parameters to win a medal",
    ],
)

if options == "Number of medals for each country":
    st.header("Number of medals for each country")
    participants_with_medal_summer = participants_with_medal[
        (participants_with_medal["Season"] == "Summer")
    ]
    participants_with_medal_winter = participants_with_medal[
        (participants_with_medal["Season"] == "Winter")
    ]

    top_countries_summer = participants_with_medal_summer.dropna(subset=["Medal"])
    top_countries_summer = (
        top_countries_summer.region.value_counts()
        .reset_index()
        .head(100)
        .merge(df, left_on="index", right_on="region", how="left")[
            ["index", "region_x"]
        ]
        .drop_duplicates("index")
    )
    top_countries_summer.rename(
        columns={"index": "region", "region_x": "Medals"}, inplace=True
    )

    top_countries_winter = participants_with_medal_winter.dropna(subset=["Medal"])
    top_countries_winter = (
        top_countries_winter.region.value_counts()
        .reset_index()
        .head(100)
        .merge(df, left_on="index", right_on="region", how="left")[
            ["index", "region_x"]
        ]
        .drop_duplicates("index")
    )
    top_countries_winter.rename(
        columns={"index": "region", "region_x": "Medals"}, inplace=True
    )

    top_countries_summer.loc[
        top_countries_summer["Medals"] < 500, "region"
    ] = "Other countries"
    fig = px.pie(
        top_countries_summer,
        values="Medals",
        names="region",
        title="Summer Season",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)

    top_countries_winter.loc[
        top_countries_winter["Medals"] < 100, "region"
    ] = "Other countries"
    fig = px.pie(
        top_countries_winter,
        values="Medals",
        names="region",
        title="Winter Season",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)
    st.subheader(
        "As we can see, the top 3 countries in summer season are USA, Russia and Germany. The top 3 "
        "countries in winter season are Russia, Canada and Germany."
    )

if options == "Number of medals for each country for each sport":
    st.header("Number of medals for each country for each sport")
    sport_for_region = (
        participants_with_medal.groupby(["region", "Sport"])["Medal"]
        .count()
        .reset_index()
    )
    fig = px.sunburst(
        sport_for_region,
        path=["region", "Sport"],
        values="Medal",
        width=800,
        height=800,
    )
    st.plotly_chart(fig)
    st.subheader(
        "Now you can read more about each country′s participation in the Olympics."
    )

if options == "All medals with descriptions of the year, country and sport":
    st.header("All medals with descriptions of the year, country and sport")
    fig = px.scatter_3d(
        participants_with_medal,
        x="region",
        y="Sport",
        z="Year",
        color="Medal",
        color_discrete_sequence=["gold", "brown", "silver"],
        template="plotly_white",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)
    st.subheader(
        "This plot gives you an opportunity to check out all the medals of the Olympics."
    )

if options == "The right parameters to win a medal":
    st.header("The right parameters to win a medal")
    lottie_coding = load_lottiefile(
        "/Users/maximsukhoparov/PycharmProjects/Streamlit_App/96783-medal-achievements.json"
    )
    lottie_hello = load_lottieurl(
        "https://assets7.lottiefiles.com/packages/lf20_x7cjigjf.json"
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
        "Based on this data, we can find the ideal height-to-weight ratio for winning a medal."
    )
    fig = px.scatter(
        participants_with_medal,
        x="Weight",
        y="Height",
        color=participants_with_medal["Medal"],
        symbol=participants_with_medal["Sex"],
        color_discrete_sequence=["gold", "brown", "silver"],
        template="plotly_white",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)
    st.subheader(
        "Now we see that most Olympic competitors are 1.5 times their weight. Therefore, based on this "
        "graph, athletes can work on their nutrition."
    )

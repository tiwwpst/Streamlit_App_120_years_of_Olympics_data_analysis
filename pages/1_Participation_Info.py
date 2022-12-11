import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display
from matplotlib import rcParams
import seaborn as sns
import plotly.express as px
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

st.set_option("deprecation.showPyplotGlobalUse", False)
st.title("Participation Info")
st.sidebar.title("Navigation")

options = st.sidebar.radio(
    "Topics:",
    options=[
        "The Number of Participants",
        "The Number of Partcipating Countries",
        "Top 20 Athletes of All Time",
    ],
)

if options == "The Number of Participants":
    st.header("The Number of Participants")
    st.subheader(
        "From year to year Olympics become more popular and significant for people."
    )
    fig = px.line(
        summer_mw_df,
        x="Year",
        y=["Male", "Female"],
        title="Summer Season",
        template="plotly_white",
        width=900,
        height=500,
    )
    fig.update_layout(yaxis_title="Number of Participants")
    st.plotly_chart(fig)

    fig = px.line(
        winter_mw_df,
        x="Year",
        y=["Male", "Female"],
        title="Winter Season",
        template="plotly_white",
        width=900,
        height=500,
    )
    fig.update_layout(yaxis_title="Number of Participants")
    st.plotly_chart(fig)
    st.subheader(
        "It is becoming apparent that over the years there are more and more participants in the Olympics, "
        "which means that the popularity of the Olympic Games is growing. Note that every 25-30 years the "
        "number of male participants drops dramatically and then rises. By comparison, the number of female "
        "participants only increases smoothly."
    )

nations_per_year_summer = (
    summer_df.drop_duplicates(["Year", "region"])["Year"]
    .value_counts()
    .reset_index()
    .sort_values("index")
)
nations_per_year_winter = (
    winter_df.drop_duplicates(["Year", "region"])["Year"]
    .value_counts()
    .reset_index()
    .sort_values("index")
)

nations_per_year_summer.rename(
    columns={"index": "Year", "Year": "Countries Participated in Summer"}, inplace=True
)
nations_per_year_winter.rename(
    columns={"index": "Year", "Year": "Countries Participated in Winter"}, inplace=True
)


if options == "The Number of Partcipating Countries":
    st.header("The Number of Partcipating Countries")
    fig = px.line(
        nations_per_year_summer,
        x="Year",
        y="Countries Participated in Summer",
        template="plotly_white",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)

    fig = px.line(
        nations_per_year_winter,
        x="Year",
        y="Countries Participated in Winter",
        template="plotly_white",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)
    st.subheader(
        "The first thing we can see from this line graph is that the Winter Olympics are half as popular as "
        "the Summer Olympics. Secondly, we can also see that more and more countries are participating in the "
        "Olympics over the years."
    )


if options == "Top 20 Athletes of All Time":
    st.header("Top 20 athletes of all time")
    lottie_coding = load_lottiefile(
        "/Users/maximsukhoparov/PycharmProjects/Streamlit_App/70671-olympic-games-2021-road-cycling.json"
    )
    lottie_hello = load_lottieurl(
        "https://assets4.lottiefiles.com/packages/lf20_tlbboysk.json"
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
    top_athletes = participants_with_medal.dropna(subset=["Medal"])
    top_athletes = (
        top_athletes.Name.value_counts()
        .reset_index()
        .head(20)
        .merge(df, left_on="index", right_on="Name", how="left")[
            ["index", "Name_x", "Sport", "region"]
        ]
        .drop_duplicates("index")
    )
    top_athletes.rename(columns={"index": "Name", "Name_x": "Medals"}, inplace=True)
    fig = px.bar(
        top_athletes,
        x="Medals",
        y="Name",
        color="region",
        width=900,
        height=500,
        color_discrete_sequence=px.colors.qualitative.Antique,
    )
    fig.update_yaxes(ticklabelposition="inside top", title=None)
    fig.update_layout(yaxis_title="Number of Participants")
    st.plotly_chart(fig)
    st.subheader(
        "As we can see, the best athletes are competing for the United States and Russia."
    )

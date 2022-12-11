import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display_functions import display
from matplotlib import rcParams
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

from Overview import (
    summer_mw_df,
    winter_mw_df,
    summer_df,
    winter_df,
    df,
    participants_with_medal,
)

st.title("Participants' Age Info")
st.sidebar.title("Navigation")
st.set_option("deprecation.showPyplotGlobalUse", False)

options = st.sidebar.radio(
    "Topics:",
    options=[
        "The Most Frequent Age",
        "Age of Participants by Year",
        "Ideal Age to Become a Medalist",
    ],
)
if options == "The Most Frequent Age":
    st.header("The most frequent age")
    st.subheader(
        "Based on my knowledge of sports, I think the most popular age is between 23 and 28."
    )
    sns.set(
        style="whitegrid",
    )
    sns.distplot(df["Age"], color="blue")
    plt.xlabel("Age of the participants", fontsize=15, weight="semibold")
    plt.ylabel("Density", fontsize=15, weight="semibold")
    sns.set(rc={"figure.figsize": (10, 5)})
    st.pyplot(plt)
    st.subheader("The graph clearly shows that the most popular age of all time is 25.")

if options == "Age of Participants by Year":
    st.header("Age of Participants by Year")
    fig = px.scatter(
        participants_with_medal,
        x="Year",
        y="Age",
        color="Sex",
        marginal_y="violin",
        trendline="ols",
        template="simple_white",
        width=900,
        height=500
    )
    st.plotly_chart(fig)
    st.subheader(
        "You can see from this plot that the average age on teams has changed over the years. About a "
        "century ago, teams selected athletes a little older, but now it is better to be younger."
    )

if options == "Ideal Age to Become a Medalist":
    st.header("Ideal Age to Become a Medalist")
    st.subheader(
        "Based on this data, I want to assume that the majority of participants receive a medal between the "
        "ages of 20 and 30."
    )
    fig = px.box(
        participants_with_medal,
        x="Medal",
        y="Age",
        color="Medal",
        color_discrete_sequence=["gold", "brown", "silver"],
        template="plotly_white",
        width=900,
        height=500,
    )
    st.plotly_chart(fig)
    st.subheader(
        "So, due to this graph i can hypothesize, that the best age to win a medal is range from 22-28. "
        "Thus, it is easy to understand the participant′s chances of winning a medal at the Olympics."
    )

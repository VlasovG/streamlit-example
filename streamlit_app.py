import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
#Добрый день! Меня зовут Власов Геннадий, данное приложение создал на основе библиотеки Streamlit!

"""

num_points = st.slider("Количество точек в спирали", 1, 10000, 1100)
num_turns = st.slider("Количество витков спирали", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

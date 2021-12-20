# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

stacked = data["model"]
columns = ['Age' , 'BMI']

def show_predict_page():
    st.title("Diabetes-Health-Indicators ")

st.write("""### We need some information for prediction""")

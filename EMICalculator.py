import streamlit as st
import numpy as np 
import pandas as pd

def calculate_emi(p, n, r):
	emi = p *(r/100)*((1+r/100)**n)/((1+r/100)**n-1)
	st.write("EMI Calculated: ", emi)
st.title("EMI Calculator")
p = st.slider("Loan Amount", 1000.0, 1000000.0)
n = st.slider("Loan Period in Years", 1, 30)
r = st.slider("Rate of Interest", 1, 15)
n = n*12
r=r/12
if st.button("Calculate"):
	calculate_emi(p, n, r)
import streamlit as sl
from matplotlib import pyplot as plt
import numpy as np

# Create a numpy array with 100 values between 0 and 10
x = np.linspace(0,10,100)

#bar chart axis
bar_x = np.array([1,2,3,4,5])


# Sidebar
opt = sl.sidebar.radio("Select Any Graph", options=("Line", "Bar", "H-Bar"))

# Graphs
if opt == "Line":
    
    sl.markdown("<h1 style='text-align:center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig= plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    sl.write(fig)

elif opt == "Bar":
    sl.markdown("<h1 style='text-align:center;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig= plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    sl.write(fig)

elif opt == "H-Bar":
    sl.markdown("<h1 style='text-align:center;'>H-Bar Chart</h1>", unsafe_allow_html=True)
    fig= plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    sl.write(fig)

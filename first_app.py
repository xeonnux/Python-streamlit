import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import http
import webbrowser
st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
d= {'First column':[1,2,3,4],
    'Second Column':[10,20,30,40],
    'Third Column':['Wayne','Damien','Future','Millionaires']
    }
st.write(pd.DataFrame(data=d))
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(data=d)
    st.line_chart(chart_data)
st.write(
    "This is bizarre too quickly modifying without having bugs issues.."
    )
if st.button('Google'):
    webbrowser.open("http://www.google.com",new=2)
    st.write('Hahaha took me 1 day to figure out in 5 minutes how to really do it')

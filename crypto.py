# -*- coding: utf-8 -*-
"""crypto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bn68pwF2gJjHmARZEX-QxkdjTqVX7ljX
"""

""" pip install -q streamlit

pip install pandas_datareader"""


import streamlit as st
import pandas_datareader.data as web
from datetime import datetime as dt, timedelta as td

st.title('GMRZ Crypto Tracker')

opts = st.selectbox('Select pair', (
    'BTC-USD', 
    'ETH-USD', 
    'BNB-USD',
    'XRP-USD',
    'LINK-USD',
    'DOGE-USD',
    'EOS-USD',
    'BSV-USD'
))

prices= web.get_data_yahoo(
    opts,
    start=dt.now() - td(days=365),
    end=dt.now())

st.line_chart(prices)
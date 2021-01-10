import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App 

Shown are the stock **closing price** and  **volume** of FATANG!

""")
company = st.selectbox('Which Company?',('Facebook','Apple', 'Tesla', 'Amazon', 'Netflix', 'Google'))
if company=='Facebook':
    tickerSymbol = 'FB'
elif company=='Apple':
    tickerSymbol = 'AAPL'
elif company=='Tesla':
    tickerSymbol = 'TSLA'
elif company=='Amazon':
    tickerSymbol = 'AMZN'
elif company=='Netflix':
    tickerSymbol = 'NFLX'
else:
    tickerSymbol = 'GOOGL'


tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-05-31', end = '2021-1-9')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
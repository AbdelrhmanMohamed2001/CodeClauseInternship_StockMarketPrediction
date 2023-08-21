import yfinance as yf
import streamlit as st

st.title("STOCK MARKET PREDICTION")

googleCheckbox= st.checkbox("Google Company")
appleCheckbox= st.checkbox("Apple Company")
amazonCheckbox= st.checkbox("Amazon Company")
microsoftCheckbox= st.checkbox("Microsoft Company")

if googleCheckbox:

   st.write("""
   **The Stock Closing Price For Google company**
   """)

   tickerSymbol = "GOOGL"
   tickerData = yf.Ticker(tickerSymbol)
   tickerdf= tickerData.history(period= "id", start= '2010-5-31', end= '2020-5-31')
   st.line_chart(tickerdf.Close)
   st.line_chart(tickerdf.Volume)


elif appleCheckbox:

   st.write("""
   **The Stock Closing Price For Apple company**
   """)

   tickerSymbol = "AAPL"
   tickerData = yf.Ticker(tickerSymbol)
   tickerdf= tickerData.history(period= "id", start= '2010-5-31', end= '2020-5-31')
   st.line_chart(tickerdf.Close)
   st.line_chart(tickerdf.Volume)

elif amazonCheckbox:

   st.write("""
   **The Stock Closing Price For Amazon company**
   """)

   tickerSymbol = "AMZN"
   tickerData = yf.Ticker(tickerSymbol)
   tickerdf= tickerData.history(period= "id", start= '2010-5-31', end= '2020-5-31')
   st.line_chart(tickerdf.Close)
   st.line_chart(tickerdf.Volume)

elif microsoftCheckbox:

   st.write("""
   **The Stock Closing Price For Microsoft company**
   """)

   tickerSymbol = "MSFT"
   tickerData = yf.Ticker(tickerSymbol)
   tickerdf= tickerData.history(period= "id", start= '2010-5-31', end= '2020-5-31')
   st.line_chart(tickerdf.Close)
   st.line_chart(tickerdf.Volume)

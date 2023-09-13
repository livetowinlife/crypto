import streamlit as st
import pandas as pd
import plotly.express as px

# Sample cryptocurrency price data (replace with your dataset)
data = pd.read_csv('data (1).csv')  # Replace with your dataset

# Streamlit app
st.title("Cryptocurrency Trading Bot")

# Sidebar for user inputs
st.sidebar.header("Trading Parameters")

# Allow users to adjust short-term and long-term moving average windows
short_window = st.sidebar.slider("Short-term Moving Average Window", 1, 100, 20)
long_window = st.sidebar.slider("Long-term Moving Average Window", 1, 200, 50)

# Calculate moving averages based on user-selected parameters
data['SMA_short'] = data['Close'].rolling(window=short_window).mean()
data['SMA_long'] = data['Close'].rolling(window=long_window).mean()

# Display price chart based on selected parameters
st.subheader("Cryptocurrency Price Chart")
fig = px.line(data, x='Date', y=['Close', 'SMA_short', 'SMA_long'],
              labels={'Close': 'Price'},
              title='Cryptocurrency Price and Moving Averages')
st.plotly_chart(fig, use_container_width=True)  # Use_container_width makes it responsive

# Simulated trading strategy (example)
st.subheader("Trading Strategy Signals (Simplified)")
data['Signal'] = 0
data.loc[data['SMA_short'] > data['SMA_long'], 'Signal'] = 1  # Buy signal
data.loc[data['SMA_short'] < data['SMA_long'], 'Signal'] = -1  # Sell signal
data['Position'] = data['Signal'].cumsum()

# Display trading signals
st.subheader("Trading Signals")
st.dataframe(data[['Date', 'Close', 'SMA_short', 'SMA_long', 'Signal', 'Position']])

# Display current position
st.subheader("Current Position")
current_position = data.iloc[-1]['Position']
st.write(f"Current Position: {current_position} coins")

# Risk management and trading actions can be implemented here in a real bot
# This is just a simplified example for educational purposes

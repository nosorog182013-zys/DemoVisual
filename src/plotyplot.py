import plotly.graph_objects as go
"""Import  plotly graphing library."""
from validata import data_validated
data3 = data_validated
"""Import data from the dataset preparation module."""
data3['Open time'] = data3['Open time'].astype(str)
"""Convert 'Open time' to string for better visualization"""
fig = go.Figure()
"""Plot figure Plot3."""
# noinspection PyTypeChecker
fig.add_trace(go.Candlestick(
    x=data3['Open time'],
    open=data3['Open'],
    high=data3['High'],
    low=data3['Low'],
    close=data3['Close'],
    increasing_line_color='green',
    decreasing_line_color='red',
    name='Candlestick'
))
"""Create candlestick chart."""
fig.add_trace(go.Scatter(
    x=data3['Open time'],
    y=data3['Volume'],
    mode='lines',
    name='Volume',
    line=dict(color='blue', width=1.5),
    yaxis='y2'
))
"""Add volume as line chart with a secondary y-axis"""
fig.update_layout(
    title='Financial Candlestick Chart',
    xaxis_title='Time',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False,  # Hide range slider for better view
    template='plotly_dark',  # Dark theme for better visibility
    height=700,
    width=1200,
    yaxis=dict(title='Price', side='left'),
    yaxis2=dict(title='Volume', overlaying='y', side='right')
)
"""Customize the layout"""
fig.show()

import seaborn as sns
"""Import package seaborn"""
import matplotlib.pyplot as plt
"""Import pyplot for simple plots."""
from validata import data_validated
data2 = data_validated
"""Import data from the dataset preparation module."""
plt.figure(figsize=(16, 10))
sns.set_theme(style="darkgrid", palette="pastel")
"""Plot figure and size Plot2."""
data2['Price Change'] = data2['Close'] - data2['Open']
data2['Color'] = data2['Price Change'].apply(lambda x: 'green' if x > 0 else 'red')
"""Calculate candle properties."""
sns.barplot(x=data2['Open time'], y=data2['Open'], hue=data2['Color'],
            data=data2, dodge=False, legend=False,
            palette={'green': 'green', 'red': 'red'})
"""Draw a histogram that looks like a candle."""
for i in range(len(data2)):
    open_time = data2.index[i]
    high = data2['High'].iloc[i]
    low = data2['Low'].iloc[i]
    close = data2['Close'].iloc[i]
    open_price = data2['Open'].iloc[i]
    plt.vlines(x=open_time, ymin=low, ymax=high, color='black', linewidth=1)
    """Draw the wicks (high-low lines) using Matplotlib vlines."""
    plt.bar(open_time, close - open_price, bottom=open_price,
            color='green' if close > open_price else 'red', width=0.5)
    """Draw the candlestick body (use Open vs Close price for height.)"""
plt.title('Candlestick Chart (Open, Close, High, Low Prices)')
plt.xlabel('Time')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.grid()
"""Titles and labels."""
plt.show()

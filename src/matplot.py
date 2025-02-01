import matplotlib.patches as mpatches
"""Import patches 2D artist."""
import matplotlib.dates as mdates
"""Import patches python datetime artist."""
import numpy as np
"""Import NumPy for handling multi-dimensional arrays."""
import matplotlib.pyplot as plt
"""Import pyplot for simple plots."""
from matplotlib.axes import Axes
"""Import axes sub-plot in figure."""
from validata import data_validated
data1 = data_validated
"""Import data from the dataset preparation module."""
ax1: Axes
fig, ax1 = plt.subplots(ncols=1, nrows=1,figsize=(16, 10))
"""Plot the figure with axis Plot1."""
def plot_candlestick(ax, data):
  for i in range(len(data)):
    """Plot candlestick chart."""
    open_price = data['Open'].iloc[i]
    close_price = data['Close'].iloc[i]
    high_price = data['High'].iloc[i]
    low_price = data['Low'].iloc[i]
    open_time = data['Open time'].iloc[i]
    close_time = data['Close time'].iloc[i]
    open_time_num = mdates.date2num(open_time)
    close_time_num = mdates.date2num(close_time)
    """Convert timestamps for matplotlib."""
    color = 'green' if close_price > open_price else 'red'
    """Determine color for the candle (green for rise, red for fall)."""
    center_time_num = (open_time_num + close_time_num) / 2
    ax.plot([center_time_num, center_time_num], [low_price, high_price], color=color, lw=0.6)
    """Plot the wick (vertical line low_price-high_price)."""
    ax.add_patch(mpatches.Rectangle((open_time_num, min(open_price, close_price)),
                                    close_time_num - open_time_num,
                                    np.abs(open_price - close_price),
                                    color=color, lw=0))
    """Plot the candle (box for open - close)."""
    ax.grid(which='major')


# noinspection PyTypeChecker
plot_candlestick(ax1, data1)
ax2 = ax1.twinx()
ax2.plot(data1['Open time'], data1['Volume'], color='blue', alpha=0.5)
"""Plot the trading volume."""
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H'))
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=4))
ax1.tick_params(axis='x', rotation=45)
"""Format x-axis."""
ax1.set_title('Price (Candlestick) and Trading Volume')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')
ax2.set_ylabel('Volume')
"""Titles and labels."""
plt.tight_layout()
plt.show()
"""Display chart."""
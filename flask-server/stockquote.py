import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and date range
stock_symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2023-01-01"

# Fetch the stock price data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Extract important financial data
stock_open = stock_data['Open']
stock_high = stock_data['High']
stock_low = stock_data['Low']
stock_close = stock_data['Close']
stock_volume = stock_data['Volume']

# Create a figure with multiple subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot the stock price chart
ax1.plot(stock_data.index, stock_close, label="Close Price", color="blue")
ax1.set_title(f"{stock_symbol} Stock Price")
ax1.set_ylabel("Price (USD)")
ax1.grid(True)
ax1.legend()

# Plot the stock volume chart
ax2.fill_between(stock_data.index, stock_volume, color="gray", alpha=0.6)
ax2.set_title(f"{stock_symbol} Stock Volume")
ax2.set_xlabel("Date")
ax2.set_ylabel("Volume")
ax2.grid(True)

# plt.tight_layout()
# plt.show()

# # Display financial data
# print(f"Stock Symbol: {stock_symbol}")
# print(f"Start Date: {start_date}")
# print(f"End Date: {end_date}")
# print(f"Summary Statistics:")
# print(stock_data.describe())


def return_stock_info(stock_symbol):
    result = []
    result.append(stock_symbol)

    return {
        "stocks_info": result
    }

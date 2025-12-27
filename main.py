import yfinance as yf

print("Infosys Stock Analysis")

stock=yf.Ticker("INFY.NS")
data=stock.history(period="5mo")

print(data.head())

print("Highest price:",data['High'].max())
print("Lowest price:", data['Low'].min())

data['Daily Return']=data['Close'].pct_change()*100
print(data[['Close','Daily Return']].tail())
data['MA20']=data['Close'].rolling(window=20).mean()
data['MA50']=data['Close'].rolling(window=50).mean()

import matplotlib.pyplot as plt

plt.plot(data['Close'],label='Close Price')
plt.plot(data['MA20'], label='20-Day Moving Average')
plt.plot(data['MA50'],label='50-Day Moving Average')

plt.title("Infosys Stock Price with Moving Averages (Last 5 Month )")
plt.xlabel("Date")
plt.ylabel(("Price(₹)"))
plt.legend()
plt.show()

data = data.round(2)
data.index = data.index.date
data.to_csv("Infosys_stock_analysis.csv")
print("Data saved to CSV file successfully")
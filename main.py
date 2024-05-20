import yfinance as yf
import sys
import time

TICKER_SYMBOL = str(sys.argv[1])
NUM_DAYS = int(sys.argv[2])

curr_time = int(time.time())
time_delta = int(24 * 60 * 60 * NUM_DAYS)
start_time = int(curr_time - time_delta)

data = yf.download(tickers=TICKER_SYMBOL, start=start_time, end=curr_time)

sum = sum(data["Close"])
avg_price = sum / len(data["Close"])
stock = yf.Ticker(ticker=TICKER_SYMBOL)

print(f"You should buy {TICKER_SYMBOL} when it is price of: {avg_price:.2f}")
if "currentPrice" not in stock.info.keys(): # For mutual funds/ETFs
  print(f"Current price of {TICKER_SYMBOL} is: {stock.info['regularMarketPreviousClose']}")
else:
  print(f"Current price of {TICKER_SYMBOL} is: {stock.info['currentPrice']}")

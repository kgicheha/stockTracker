from flask import Flask, request, jsonify
import stockquote
import yfinance as yf
import matplotlib.pyplot as plt
import subprocess

app = Flask(__name__)

# Define the stock symbol and date range
stock_symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2023-01-01"

# Fetch the stock price data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# home page
@app.route("/quote")
def display_quote():

    # get a stock ticker symbol from the query string
    symbol = request.args.get('symbol', default ="AAPL")

    # pull the stock quote
    quote = yf.Ticker(symbol)

    #return the object via the HTTP Response
    return jsonify(quote.info)

# DISPLAY ALL ITEMS IN THE compareList
@app.route("/comparelist")
def watch_list():
    return {
        "stocks": [
            "Apple",
            "Google",
            "Microsoft"
        ]
    }

# ADDING ITEMS TO compareList

# REMOVING ITEM FROM compareList

# UPDATING ITEM PRICE IN THE compareList

# DELETING ITEM FROM compareList



if __name__ == "__main__":
    app.run(debug=True)



#!/usr/bin/python

#this is a test script; it will get latest stock prices
import request2
import yfinance as yf
import sys
import time

def main():
    print("Hello Contianer!")
    if len(sys.argv) < 1:
        print("You need to provide a stock ticker")
        exit
    else:
        ticker = sys.argv[1]
        while True:
            recent_data = yf.download(ticker, period="5d")
            print(recent_data)
            time.sleep(30)

if __name__ == "__main__":
    main()

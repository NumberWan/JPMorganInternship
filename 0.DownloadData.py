#It is the program for download the data form Yahoo Finance

import yfinance as yf
import pandas   as pd
import csv

dow30 = pd.read_csv('dow30list.csv')

# There there is only one html table on this Yahoo! Finance page
payload=pd.read_html('https://finance.yahoo.com/quote/%5EHSI/components/')
print(payload)
table_0 = payload[0]
df = table_0
print(df.head())
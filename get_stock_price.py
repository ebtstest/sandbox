from yahoo_finance import Share
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import csv
import os
style.use('ggplot')

#Pandas DataFrame four ways --> "concat, append, merge, join"


#
#Get Stock price quote from yahoo_finance module
#

##stock_list= ['TSLA', "GOOGL", "AMZN", "FB", "LNKD", "AAPL", "USO", "EBAY", "MSFT", "PFE", "MCD", "M", "QQQ", "SPY"]
##for i in stock_list:
##   ticker = Share(i)
##   data = ticker.get_historical('1990-01-01','2016-05-10')
##   column_name = list(data[0].keys())
##   print(column_name)
##   csv_filename=i+'.csv'
##   with open(csv_filename, 'w') as f:
##      w = csv.DictWriter(f, fieldnames=column_name)
##      w.writeheader()
##      for day_value in data:
##         w.writerow(day_value)

#
#Get Stock price quote from Pandas.io.data
#

##start = datetime.datetime(2016,1,5)
##end = datetime.datetime(2016,5,5)
##df = web.DataReader("TSLA", "yahoo", start, end)
##print(df.head())
##df['Adj Close'].plot()
##plt.show()

#
#Create new csv files with Date as index
#

##stock_list= ['TSLA', "GOOGL", "AMZN", "FB", "LNKD", "AAPL", "USO", "EBAY", "MSFT", "PFE", "MCD", "M", "QQQ", "SPY"]
##
##for i in stock_list:
##    filename=i+".csv"
##    print(filename)
##    filename_new=i+"_new.csv"
##    df = pd.read_csv(filename)
##    df.set_index('Date', inplace=True)
##    #print(df.head())
##
##    df.columns = [i+'_Open',i+'_Volume',i+'_Symbol',i+'_High',i+'_Close',i+'_Adj_Close',i+'_Low']
##    print(df.head())
##
##    df.to_csv(filename_new)

#
#Create new DataFrame by joining all invidual DataFrames 
#

###stock_list= ['TSLA', "GOOGL", "AMZN", "FB", "LNKD", "AAPL", "USO", "EBAY", "MSFT", "PFE", "MCD", "M", "QQQ", "SPY"]
###joined = pd.read_csv("TSLA_new.csv", index_col=0)
##joined = pd.read_csv("TSLA_new.csv", index_col=0)
##
##for i in stock_list[1:]:
##    filename=i+"_new.csv"
##    filename_new="stock_quote.csv"
##    df = pd.read_csv(filename, index_col=0)
##    print(df.head())
##    #joined = joined.merge(df, on='Date')
##    joined = joined.join(df, how='outer')
##print(joined.head())
##joined.to_csv(filename_new)

##df = pd.read_csv('stock_quote.csv', index_col=0)
##print(df.head())
##stock_list= ['TSLA', "GOOGL", "AMZN", "FB", "LNKD", "AAPL", "USO", "EBAY", "MSFT", "PFE", "MCD", "M", "QQQ", "SPY"]
##title_list_delete=[]
##for i in stock_list:
##   title_list_delete.append(i+'_Symbol')
##print(title_list_delete)
##df.drop(title_list_delete, inplace=True, axis=1)
##print(df.head())
##df.to_csv('stock_quote_new.csv')


stock_list= ['TSLA', "GOOGL", "AMZN", "FB", "LNKD", "AAPL", "USO", "EBAY", "MSFT", "PFE", "MCD", "M", "QQQ", "SPY"]
df = pd.read_csv('stock_quote_new.csv', index_col=0)
chart_columns=[]
for i in stock_list:
   chart_columns.append(i+'_Adj_Close')
print(chart_columns)
df[chart_columns].plot()
plt.show()

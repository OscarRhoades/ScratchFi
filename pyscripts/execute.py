import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def then(arg1, arg2):


    # plt.plot( arg1, 'o')
    # plt.plot( arg2, 'o')
    # plt.show()

    then = pd.merge(arg1, arg2,  how = "left", on = "Date")
    
    # print("validity:" + str(len(then.dropna())/len(arg1)))
    # print(len(then.dropna()))
    # print(len(arg1))

    # plt.plot( then['Close_x_x'], 'o')
    # plt.plot( then['Close_x_y'], 'o')
    # plt.show()
    
    return then


def ticker(tkr_str):
    tkr = yf.Ticker(tkr_str).history(period="8mo")
    # print(tkr)
    return tkr["Close"]


def n_time_average(tkr, days):
    # numeric function
    lastdayfrom = pd.Timestamp.now() 

    # ndf = tkr.set_index('Date')
    # #if datetimeindex isn't order, order it
    # ndf = ndf.sort_index()
    #last 30 days of date lastday

    ndf = tkr.loc[lastdayfrom - pd.Timedelta(days=days):lastdayfrom].reset_index()

    return ndf["Close"].mean()

def oversold(arg1, window, p):
    # needes to have a single column
    return arg1.rolling(window=window).quantile(p)
    

# .iloc[:,0]

def compair_filter(arg1, arg2, direction):

    # filters arg1 when arg1 is greater/less than than arg2
    # if direction is true, then it is greater than
    

    filter = pd.merge(arg1, arg2, on = "Date").dropna()
    # print(filter)
    if direction:
        filter = filter.loc[filter.iloc[:,0] > filter.iloc[:,1]]
    else:
        filter = filter.loc[filter.iloc[:,0] < filter.iloc[:,1]]
    return filter.iloc[:,0]

def moving_average(tkr, window):
    # needs to have a single column

    # this gives a dataframe
    # Make this open/close an advanced option parameter
    moving_average = tkr.rolling(window=window).mean()
    return moving_average


# when amazon is higher than its moving average
# print(len(ticker("BTC-USD")))
# print(len(compair_filter(ticker("BTC-USD"), moving_average(ticker("BTC-USD"), 15))))

# compute = then(compair_filter(ticker("AMZN"), moving_average(ticker("AMZN"), 30)), compair_filter(ticker("GLD"), moving_average(ticker("GLD"), 30)))



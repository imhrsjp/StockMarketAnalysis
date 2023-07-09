import requests
DATA_AVAILABLE = False

def getUserDataKey(func_value, duration):
    if func_value == 'TIME_SERIES_INTRADAY':
        if duration == '1min':
            return 'Time Series (1min)';
        elif duration == '5min':
            return 'Time Series (5min)'
        else:
            return 'Time Series (15min)'
    elif func_value == 'TIME_SERIES_DAILY_ADJUSTED':
        return 'Time Series (Daily)'
    elif func_value == 'TIME_SERIES_WEEKLY':
        return 'Weekly Time Series'
    elif func_value == 'TIME_SERIES_WEEKLY_ADJUSTED':
        return 'Weekly Adjusted Time Series'
    elif func_value == 'TIME_SERIES_MONTHLY':
        return 'Monthly Time Series'

def getDataFromAPI(func_value, stock_symbol, duration):
    global DATA_AVAILABLE
    API_URL = "https://www.alphavantage.co/query?function={}&symbol={}&outputsize=full&interval={}&datatype=json&apikey=".format(
        func_value, stock_symbol, duration)
    data = requests.get(API_URL)
    userData = data.json()
    DATA_AVAILABLE = True
    key = getUserDataKey(func_value, duration)
    return userData['Meta Data'], userData[key]

import helpers

_5MIN = 300
_15MIN = 900
_30MIN = 1800
_2HR = 7200
_4HR = 14400
_DAY = 86400

def get_chart(pair, start, period):
    url = 'https://poloniex.com/public?command=returnChartData&currencyPair='+str(pair)+'&start='+str(start)+'&end=9999999999&period=' + str(period)
    return helpers.http_get(url)

def get_ticker():
    return helpers.http_get('https://poloniex.com/public?command=returnTicker')

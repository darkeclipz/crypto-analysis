import bittrex
import poloniex
import helpers
import datetime
import time

def get_data():
    '''
    Get all the market data from the Bittrex API.
    '''
    return {m['MarketName']:m for m in bittrex.get_ticker()['result']}

def track(symbol, price, data):
    '''
    Calculate the P/L for current bags.
    '''
    last = data[symbol]['Last']
    pl = 1 - price / last
    return [symbol, price, last, pl]

# Current bag
my_bag = [['BTC-BCC', 0.07673454], ['BTC-XVG', 0.00000103], ['BTC-WAVES', 0.00164500], ['BTC-PTOY', 0.00008030], ['BTC-LBC', 0.00014731]]

# Main functionality to execute
def main():
    # Get the data and calculate P/L  
    data = get_data()
    trackers = {x[0]:track(x[0],x[1],data) for x in my_bag}

    # Calculate BTC information
    btc = poloniex.get_chart('USDT_BTC', helpers.get_unix_time_minus_days(7),poloniex._2HR)
    btc_avg_period = 5
    btc_avg = sum([x['close'] for x in btc[-btc_avg_period:]]) / btc_avg_period
    btc_last = btc[len(btc)-1]['close']
    btc_div = 1 - btc_avg / btc_last

    # Other
    display_warning_percentage = -10

    # Display general information
    print('-- General information --')
    print('Total coins: ' + str(len(trackers)))
    print('Total P/L: ' + str(round(sum([x[3] for x in trackers.values()])*100,2)) + '%')
    print('Current BTC price (PLNX): ' + str(btc_last))
    print('Avg BTC price ('+str(btc_avg_period)+'): ' + str(btc_avg))
    print('BTC is going: ' + ('DOWN' if btc_last < btc_avg else 'UP'))
    print('BTC % from AVG: ' + str(round(btc_div * 100, 2)) + '%')
    print('-- Bags --')

    # Display bag information
    for t in trackers.values():
        print( t[0] + ' Price: ' + str(t[1]) + ' / Last: ' + str(t[2]) + ' / P&L: ' + str(round(t[3]*100,2)) + '%' + (' --WARNING!!' if t[3]*100<=display_warning_percentage else '') )


while(True):
    print('==== ' + str(datetime.datetime.now()) + ' ====')
    main()
    print('<end>')
    time.sleep(10)
        

import helpers

def get_ticker():
    return helpers.http_get('https://bittrex.com/api/v1.1/public/getmarketsummaries')

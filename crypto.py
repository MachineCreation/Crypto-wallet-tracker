# import requests
# from datetime import datetime, timedelta
import decimal as D


# API calls

def get_30day_percent(coin, day=''):
    # #  get now price
    # response1 = await requests.get(f'https://api.exchange.coinbase.com/products/{coin}-USD/ticker')
    # today_price = response1.json()[4]

    # # get 1 year ago price
    # year = day - timedelta(days=365)
    # start = (year - timedelta(days=2)).isoformat()
    # end = year.isoformat()
    # response2 = await requests.get(f'https://api.exchange.coinbase.com/products/{coin}-USD/candles/?start={start}&end={end}&granularity=86400')
    # one_year_price = response2.json()[0][4]

    # not going to make you download and go through all the env stuff to 
    # run this so I'm adding static variables for this assignment 
    if coin == 'BTC':
        today_price = 109822.32
        one_year_price = 60145.01
    if coin == 'LTC':
        today_price = 89.81
        one_year_price = 65.41
    if coin == 'ETH':
        today_price = 2596.32
        one_year_price = 3058.89
    if coin == 'XTZ':
        today_price = 0.554
        one_year_price = 0.681
    if coin == 'SOL':
        today_price = 152.6
        one_year_price = 127.83

    one_year_perc = (D.Decimal(today_price) / D.Decimal(one_year_price) - 1).quantize(D.Decimal('0.001'))
    one_month_perc = one_year_perc / 12

    return one_month_perc
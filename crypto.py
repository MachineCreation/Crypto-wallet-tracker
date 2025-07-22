
# pip modules
import requests

# python modules
import json
from datetime import date, datetime, timedelta

# local modules
import decimal as D
import memoryRetrieval as MR
import constants as Con

# API endpoints

rawAssetsEndpoint = f'https://api.coinbase.com/v2/assets/search?base=USD'

# API calls

def getCoinTicker(coin, support = False):
    '''
    validates fetch to coinbase API and returns coin data or None
    :args: coin: string
    :inputs: None 
    :return: None | json data object
    '''
    try:
        response = requests.get(f'https://api.exchange.coinbase.com/products/{coin}-USD/ticker')
        if response.ok:
            # print(response.json())
            return response.json()
        else:
            raise ValueError
    except ValueError:
        print(f'{coin} data not supported')
        if support:
            print('Not added to support list')
        return None

def getCoinHistoricalData(coin, start, end, granularity = 86400, support = False):
    '''
    validates coin historical data and returns data or None
    :args: coin: string, day: string
    :inputs: None 
    :return: None | json data object
    '''
    try:
        response = requests.get(f'https://api.exchange.coinbase.com/products/{coin}-USD/candles/?start={start}&end={end}&granularity={granularity}')
        
        if response.ok:
            return response.json()
        else:
            raise ValueError
    except ValueError:
        print(f'{coin} histories not supported')
        if support:
            print('Not added to support list')
        return None

def compileSupportedCoinsList(numCoins):
    '''
    create a list of coin symbols to use as menu options
    :args: None
    :inputs: None 
    :return: None | json data list
    '''
    supportedCoins = []
    try:
        response = requests.get(rawAssetsEndpoint) # get raw list of coins

        data = response.json()['data']
        # print(data['data'][0]['symbol'])
        # get day data for histories
        day = date.today()
        year = day - timedelta(days=365)
        # convert to iso format for coinbase
        start = (year - timedelta(days=2)).isoformat() # add 2 days padding to return 1 full day object
        end = year.isoformat()

        # loop data to find usable coins to add to list
        for coin in data:
            coin = coin['symbol']   # get coin symbol
            response1 = getCoinTicker(coin, True)
            if response1:           # validate coin ticker
                response2 = getCoinHistoricalData(coin, start, end, support=True)
                if response2 and len(supportedCoins) < numCoins:       # validate coin history
                    supportedCoins.append(coin)
                else:
                    break
            # print(f'{coin} supported: {response1.ok}')

        if supportedCoins != []:
            MR.makeJson(supportedCoins, 'coin_list')
            return supportedCoins

    except ValueError as e:
        print(f'An error occurred fetching coin list: {e}')


def get_30day_percent(coin, day):
    #  get now price
    response1 = getCoinTicker(coin)
    # print(response1)
    today_price = response1['price']

    # get 1 year ago price
    year = day - timedelta(days=365)
    start = (year - timedelta(days=2)).isoformat()
    end = year.isoformat()
    response2 = requests.get(f'https://api.exchange.coinbase.com/products/{coin}-USD/candles/?start={start}&end={end}&granularity=86400')
    one_year_price = response2.json()[0][4]

    # not going to make you download and go through all the env stuff to 
    # run this so I'm adding static variables for this assignment 
    # if coin == 'BTC':
    #     today_price = 109822.32
    #     one_year_price = 60145.01
    # if coin == 'LTC':
    #     today_price = 89.81
    #     one_year_price = 65.41
    # if coin == 'ETH':
    #     today_price = 2596.32
    #     one_year_price = 3058.89
    # if coin == 'XTZ':
    #     today_price = 0.554
    #     one_year_price = 0.681
    # if coin == 'SOL':
    #     today_price = 152.6
    #     one_year_price = 127.83

    one_year_perc = (D.Decimal(today_price) / D.Decimal(one_year_price) - 1).quantize(D.Decimal('0.001'))
    one_month_perc = one_year_perc / 12

    return one_month_perc
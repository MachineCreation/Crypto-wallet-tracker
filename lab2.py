#!/usr/bin/env python3

# ----------------------------------------------------------------------------
# Joseph Egan
# Lab 2

# Personal Crypto Investment Tracker
# This program prompts helps its user by manually storing a list of investments
# and then automatically projecting the 30 day return based on historical data 
# for that coin

# Inputs: float investment_amount, string Coin_name, string more('y','n')
# Outputs: float totalCost, float shipping, float tax, float grandTotal
# source: lab 2 assignment specs
# ----------------------------------------------------------------------------
#  sample run
# ------------------------------------------------------------------------------

# Welcome to the Crypto Investment Tracker app
# Here you can log and track your different investments and get a 30 day projected growth based on your coin's previous 12 months.

# ------------------------------------------------------------------------------

# Please choose coin from list
# -BTC
# -LTC
# -ETH
# -XTZ
# -SOL
# sol

# Enter the dollar amount you would like to invest
#  --Example: 10.00
# 1000

# Asset                                      SOL
# Total Investment                      $1000.00
# Last investment date                  07-04-25
# 30 day projection                     $1016.17

# Enter what you would like to do from the choices below
# -add
# -view
# -quit

# add

# Please choose coin from list
# -BTC
# -LTC
# -ETH
# -XTZ
# -SOL
# xtz

# Enter the dollar amount you would like to invest
#  --Example: 10.00
# 3000

# Asset                                      XTZ
# Total Investment                      $3000.00
# Last investment date                  07-04-25
# 30 day projection                     $2953.50

# Enter what you would like to do from the choices below
# -add
# -view
# -quit

# view

# Asset                                      SOL
# Total Investment                      $1000.00
# Last investment date                  07-04-25
# 30 day projection                     $1016.17

# Asset                                      XTZ
# Total Investment                      $3000.00
# Last investment date                  07-04-25
# 30 day projection                     $2953.50

# Number of assets                             2
# Total investments                     $4000.00
# 30 Day projection                     $3969.67

# Press enter to continue.

# Enter what you would like to do from the choices below
# -add
# -view
# -quit

# quit

# ------------------------------------------------------------------------------


# Have a wonderful day!
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# Welcome to the Crypto Investment Tracker app
# Here you can log and track your different investments and get a 30 day projected growth based on your coin's previous 12 months.

# ------------------------------------------------------------------------------

# Enter what you would like to do from the choices below
# -add
# -view
# -quit

# view

# Asset                                      SOL
# Total Investment                      $1000.00
# Last investment date                  07-04-25
# 30 day projection                     $1016.17

# Asset                                      XTZ
# Total Investment                      $3000.00
# Last investment date                  07-04-25
# 30 day projection                     $2953.50

# Number of assets                             2
# Total investments                     $4000.00
# 30 Day projection                     $3969.67

# Press enter to continue.

# Enter what you would like to do from the choices below
# -add
# -view
# -quit

# quit

# ------------------------------------------------------------------------------


# Have a wonderful day!
# ------------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# Python modules
import decimal as D
from datetime import date

# Local modules
import messages as M            # personal reusable messages module
import validations as V         # personal validations module
import memoryRetrieval as MR    # personal persistent memory module
import crypto as C              # API calls to coinbase for histories

def main():
    # main function variables
    APP_NAME = 'Crypto Investment Tracker'
    DESCRIPTION_STR = 'Here you can log and track your different investments and get a 30 day projected growth based on your coin\'s previous 12 months.'
    MEMORY_ADDRESS = 'app_memory'
    COINS = ['BTC', 'LTC', 'ETH', 'XTZ', 'SOL']
    
    # delineate start
    M.printDelineator()

    # welcome message
    M.welcomeMessage(APP_NAME, DESCRIPTION_STR)
    M.printDelineator()

    # get the app persistent memory dict
    memory = load_memory(MEMORY_ADDRESS)

    # run main memory loop
    memory = run_menu(memory, COINS)

    # save memory to json file(persistent)
    MR.makeJson(memory, MEMORY_ADDRESS)

    # delineate end
    M.printDelineator()

    # exit message
    M.exitMessage()
    M.printDelineator()

def load_memory(address):
    '''
    attempts to load existing memory as dict if existing memory file does
    not exist returns an empty dict
    :args: address: string
    :inputs: None
    :return: memory: Dictionary object
    '''
    memory = MR.getJson(address)
    if memory != FileNotFoundError and isinstance(memory, dict):
        return memory
    else:
        return {}
    
def run_menu(memory, coins):
    '''
    Starts main menu loop to add new investment to portfolio or view portfolio
    :args: memory: dictionary object
    :inputs: None
    :return: None
    '''
    options = ['add', 'view', 'quit']       # normally wouldn't create a constant here. might move it later
    while True:
            
        if memory != {}:    
            # print menu to user
            M.print_menu_options(options)
            print()     #add blank line for cleaner terminal

            # get and validate choice
            choice = V.validateChoiceFromList(options)
            print()     #add blank line for cleaner terminal
            
            if choice == 'add':
                memory = add_to_portfolio(coins, memory)
            elif choice == 'view':
                view_portfolio(memory)
            else:
                return memory
        else:
            memory = add_to_portfolio(coins, memory)

def add_to_portfolio(coins_list, memory):
    '''
    prompts user to add a coin from a list of available assets 
    and an investment amount for the asset. Then calculates the total amount 
    invested for that asset and the projected 30 day growth for that asset.
    Then returns asset, total investment for asset, date, and 30 day projection
    as a dictionary object and saves it to the main memory dict
    :args: coins_list: string List
    :inputs: coin: string, investment: float
    :return: memory: dictionary object
    '''

    coin_prompt = 'Please choose coin from list'
    investment_prompt = 'Enter the dollar amount you would like to invest\n --Example: 10.00\n'

    M.print_menu_options(coins_list, coin_prompt)

    # get asset name
    asset = V.validateChoiceFromList(coins_list, prompt=coin_prompt, case='upper')
    print()     #add blank line for cleaner terminal

    # get asset amount
    investment = D.Decimal(V.get_real(prompt=investment_prompt)).quantize(D.Decimal('0.01'))
    print()     #add blank line for cleaner terminal

    # get today's date
    day = date.today()
    day = day.strftime('%m-%d-%y')

    # get 30day projection percent
    percent30 = C.get_30day_percent(asset, day)

    # check if the asset exists in memory
    if asset in list(memory.keys()):
        # print(memory[asset][name])
        t_investment = D.Decimal(memory[asset]['investment'])   # get asset previous investment as decimal
        t_investment += investment                              # add previous investment to new investment
        memory[asset]['investment'] = str(t_investment)         # set new total investment as string
        memory[asset]['doi'] = day                              # set latest date of investment
        #calculate 30day projection
        memory[asset]['30day'] = str(t_investment + (investment * percent30).quantize(D.Decimal('0.01')))

    else: # set dict values for non-existent key 
        memory[asset] = {}
        memory[asset]['name'] = asset
        memory[asset]['investment'] = str(investment)
        memory[asset]['doi'] = day
        memory[asset]['30day'] = str(investment + (investment * percent30).quantize(D.Decimal('0.01')))
    
    print_investment(memory[asset])
    return memory
    
def print_investment(coin_i_dict):
    '''
    prints the asset name, investment amount, date of investment, and 30 day
    projection
    :args: coin_i_dict: dictionary object
    :inputs: None
    :return: None
    '''
    print(f'{'Asset':25} {coin_i_dict["name"]:>20}\n'
          f'{'Total Investment':25} {'$' + coin_i_dict["investment"]:>20}\n'
          f'{'Last investment date':25} {coin_i_dict["doi"]:>20}\n'
          f'{'30 day projection':25} {'$' + coin_i_dict["30day"]:>20}\n'
          )
    
def view_portfolio(memory):
    '''
    prints the full portfolio to the user for their viewing pleasure
    :args: memory: dictionary Object
    :inputs: finished: boolean
    :return: None
    '''
    assets = list(memory.keys())    # make a list of keys to loop through
    total_investments = 0
    number_of_assets = 0
    total_projected = 0
    for asset in assets:            # loop through keys
        coin = memory[asset]
        total_investments += D.Decimal(coin['investment'])
        number_of_assets += 1
        total_projected += D.Decimal(coin['30day'])
        print_investment(coin)
    
    # print total of portfolio values
    print(
        f'{'Number of assets':25} {number_of_assets:>20}\n'
        f'{'Total investments':25} {'$' + str(total_investments):>20}\n'
        f'{'30 Day projection':25} {'$' + str(total_projected):>20}\n'
    )
    # wait for user to finish viewing portfolio
    finished = input('Press enter to continue.\n')
    

if __name__ == "__main__":
    main()


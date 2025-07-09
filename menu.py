

# python modules
from datetime import date
import decimal as D

# local modules
import messages as M            # personal reusable messages module
import validations as V         # personal validations module
import crypto as C              # crypto currency module
import memoryRetrieval as MR    # personal persistent memory module


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

    # ---get asset name
    asset = V.validateChoiceFromList(coins_list, prompt=coin_prompt, case='upper')
    print()     #add blank line for cleaner terminal

    # ---get asset amount
    # investment = D.Decimal(V.get_real(prompt=investment_prompt)).quantize(D.Decimal('0.01'))
    # use new currency format validator
    investment = V.validateCurrencyUS(preprompt=investment_prompt)
    print()     #add blank line for cleaner terminal

    # ---get today's date
    day = date.today()
    dayStr = day.strftime('%m-%d-%y')

    # ---get 30day projection percent
    percent30 = C.get_30day_percent(asset, day)

    # check if the asset exists in memory
    if asset in list(memory.keys()):
        # print(memory[asset][name])
        t_investment = D.Decimal(memory[asset]['investment'])   # get asset previous investment as decimal
        t_investment += investment                              # add previous investment to new investment
        memory[asset]['investment'] = str(t_investment)         # set new total investment as string
        memory[asset]['doi'] = dayStr                           # set latest date of investment
        #calculate 30day projection
        memory[asset]['30day'] = str(t_investment + (investment * percent30).quantize(D.Decimal('0.01')))

    else: # set dict values for non-existent key 
        memory[asset] = {}
        memory[asset]['name'] = asset
        memory[asset]['investment'] = str(investment)
        memory[asset]['doi'] = dayStr
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
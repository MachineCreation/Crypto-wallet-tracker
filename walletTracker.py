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
# -ETH
# -USDT
# -XRP
# -SOL
# btc

# Enter the dollar amount you would like to invest
#  --Example: 10.00

# Enter number in valid US currency format.
# Example: $1 = 1.00
# 0
# Invalid entry!
# Enter number in valid US currency format.
# Example: $1 = 1.00
# 0.00

# Asset                                      BTC
# Total Investment                         $0.00
# Last investment date                  07-16-25
# 30 day projection                        $0.00

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# add

# Please choose coin from list
# -BTC
# -ETH
# -USDT
# -XRP
# -SOL
# sol

# Enter the dollar amount you would like to invest
#  --Example: 10.00

# Enter number in valid US currency format.
# Example: $1 = 1.00
# 1000.89

# Asset                                      SOL
# Total Investment                      $1000.89
# Last investment date                  07-16-25
# 30 day projection                     $1004.48

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# view

# Asset                                      BTC
# Total Investment                         $0.00
# Last investment date                  07-16-25
# 30 day projection                        $0.00

# Asset                                      SOL
# Total Investment                      $1000.89
# Last investment date                  07-16-25
# 30 day projection                     $1004.48

# Number of assets                             2
# Total investments                     $1000.89
# 30 Day projection                     $1004.48

# Press enter to continue.

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# delete

# Please choose investment you would like to delete
#  or type quit to go back to the main menu
# -BTC
# -SOL
# -QUIT
# btc
# Are you sure you want to remove BTC
# continue? y/n
# y
# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# delete

# Please choose investment you would like to delete
#  or type quit to go back to the main menu
# -SOL
# -QUIT
# sol
# Are you sure you want to remove SOL
# continue? y/n
# n
# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# view

# Asset                                      SOL
# Total Investment                      $1000.89
# Last investment date                  07-16-25
# 30 day projection                     $1004.48

# Number of assets                             1
# Total investments                     $1000.89
# 30 Day projection                     $1004.48

# Press enter to continue.

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# delete

# Please choose investment you would like to delete
#  or type quit to go back to the main menu
# -SOL
# -QUIT
# quit
# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit

# quit

# ------------------------------------------------------------------------------


# Have a wonderful day!
# ------------------------------------------------------------------------------

# Would you like to run the wallet again? Y/N?
# n
# ----------------------------------------------------------------------------


# Python modules

# Local modules
import messages as M            # personal reusable messages module
import validations as V         # personal validations module
import memoryRetrieval as MR    # personal persistent memory module
import constants as Con         # program constant variables
import menu                     # main menu module

def main():
    while True:

        # run main program loop
        start()

        if V.get_Y_N('Would you like to run the wallet again? Y/N?\n') == 'n':
            break

def start():
    # main function variables moved to constants.py
    
    # delineate start
    M.printDelineator()

    # welcome message
    M.welcomeMessage(Con.APP_NAME, Con.DESCRIPTION_STR)
    M.printDelineator()

    # get the app persistent memory
    coins = MR.load_memory_list(Con.COINS)
    memory = MR.load_memory_dict(Con.MEMORY_ADDRESS)

    # run main menu loop moved to menu.py
    memory = menu.run_menu(memory, coins)

    # save memory to json file(persistent)
    MR.makeJson(memory, Con.MEMORY_ADDRESS)

    # delineate end
    M.printDelineator()

    # exit message
    M.exitMessage()
    M.printDelineator()

if __name__ == "__main__":
    main()


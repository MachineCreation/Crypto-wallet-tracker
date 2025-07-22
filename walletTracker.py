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
# -XRP
# -USDT
# -SOL
# -DOGE
# -ADA
# -XLM
# -SUI
# -LINK
# -HBAR
# -AVAX
# -BCH
# -LTC
# -SHIB
# shib

# Enter the dollar amount you would like to invest
#  --Example: 10.00

# Enter number in valid US currency format.
# Example: $1 = 1.00
# 1000.00

# Asset                                     SHIB
# Total Investment                      $1000.00
# Last investment date                  07-22-25
# 30 day projection                      $988.50

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit
# -refresh

# add

# Please choose coin from list
# -BTC
# -ETH
# -XRP
# -USDT
# -SOL
# -DOGE
# -ADA
# -XLM
# -SUI
# -LINK
# -HBAR
# -AVAX
# -BCH
# -LTC
# -SHIB
# sui

# Enter the dollar amount you would like to invest
#  --Example: 10.00

# Enter number in valid US currency format.
# Example: $1 = 1.00
# 2500.00

# Asset                                      SUI
# Total Investment                      $2500.00
# Last investment date                  07-22-25
# 30 day projection                     $3277.71

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit
# -refresh

# refresh

# Please enter the number of coins you would like to view
# upto 15
# 5

# ETH2 data not supported
# Not added to support list
# BNB data not supported
# Not added to support list
# USDC data not supported
# Not added to support list

# Your coin list length has been updated to 5

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit
# -refresh

# add

# Please choose coin from list
# -BTC
# -ETH
# -XRP
# -USDT
# -SOL
# xrp

# Enter the dollar amount you would like to invest
#  --Example: 10.00

# Enter number in valid US currency format.
# Example: $1 = 1.00
# 4500.00

# Asset                                      XRP
# Total Investment                      $4500.00
# Last investment date                  07-22-25
# 30 day projection                     $6313.12

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit
# -refresh

# view

# Asset                                     SHIB
# Total Investment                      $1000.00
# Last investment date                  07-22-25
# 30 day projection                      $988.50

# Asset                                      SUI
# Total Investment                      $2500.00
# Last investment date                  07-22-25
# 30 day projection                     $3277.71

# Asset                                      XRP
# Total Investment                      $4500.00
# Last investment date                  07-22-25
# 30 day projection                     $6313.12

# Number of assets                             3
# Total investments                     $8000.00
# 30 Day projection                    $10579.33

# Press enter to continue.

# Enter what you would like to do from the choices below
# -add
# -view
# -delete
# -quit
# -refresh

# quit

# ------------------------------------------------------------------------------


# Have a wonderful day!
# ------------------------------------------------------------------------------

# Would you like to run the wallet again? Y/N?
# n
# ------------------------------------------------------------------------------

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


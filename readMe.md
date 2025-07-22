# Welcome to the basic crypto wallet tracker

(This readme is best viewed in a markdown viewer)

Good Morning! it is that time in the lifecycle of a program where a read me file is necessary to impart the proper usage of the program. The following are instructions for VScode so yours might be a little different. 

## contents

[Download](#download)\
[Setup](#setup)\
[Startup](#startup)\
[Major Versions and Updates](#major-versions-and-updates)

## download
If you do not already have the project folder downloaded to your workstation feel free to clone the repository <a href='https://github.com/MachineCreation/Crypto-wallet-tracker.git'>here</a>.

## setup

Once the files are downloaded to your machine, it is best practice to set up a virtual environment use the following script in terminal\

note that this process assumes python3 is installed on your machine.

    $ python -m venv .venv

activate virtual environment

    $ .venv/Scripts/Activate

next download and install required modules

    $ pip install -r requirements.txt

this will get all the required mods to run the program

## startup

assuming that you have followed all the steps be sure that your language mode is set to python 3.13.3(.venv: venv)

Now you can run the program locally by pressing the play icon in the top right corner of your screen in the lab2.py file or in terminal navigate to the root folder(\walletTracker) and use the following command

    $ python walletTracker.py

## major versions and updates

|   <span style='color:green'>commit</span>   | description | <span style='color: gold'>new files |
|:----------:|:-----------------------------------:|:-------:|
| <span style='color:green'>07082025 | Initial commit including first working version of the wallet investment tracker | <span style='color: gold'>crypto.py</br> lab2.py</br> memoryRetrieval.py</br> messages.py</br> unitTester.py</br> validations.py</br> .gitignore</span>
| <span style='color:green'> 07092025 | Added:</br> -validateCurrencyUS function to validations.py</br>-getCoinTicker getCoinHistoricalData compileSupportedCoinsList to crypto.py<br>-start function to walletTracker.py<br><br> Moved:</br>-run_menu to menu.py</br> -load_memory to memoryRetrieval.py</br></br>Modified:<br>-get_30day_percent in crypto.py<br><br> | <span style='color: gold'>readMe.md</br> constants.py</br> menu.py<br>coin_list.json<br> requirements.txt |
| <span style='color:green'> 07162025 | Added:<br>delete_from_portfolio() to menu.py<br>printConfirmation() to messages.py | <span style='color: gold'>** |
| <span style='color:green'> 07222025 | Added:<br>refresh_supported_coins_list() to menu.py | <span style='color: gold'>** |
| <span style='color:green'> ** | *** | <span style='color: gold'>** |
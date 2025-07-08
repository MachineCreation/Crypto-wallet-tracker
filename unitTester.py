import messages as M
import validations as V
import memoryRetrieval as MR
import crypto as C
import lab2 as L2
from datetime import datetime, timedelta

# test welcome message

# M.welcomeMessage('crypto')
# M.welcomeMessage('crypto', "pickles are the best")
# ------------------------------------------------------------------------------

# test main menu loop

# L2.run_menu()

# options = ['add', 'view']
# M.print_menu_options(options
# V.validateChoiceFromList(options)

memory = {}
COINS = ['BTC', 'LTC', 'ETH', 'XTZ', 'SOL', 'SHIB']
d = L2.add_to_portfolio(COINS, memory)
print(d)

# test = {
#     'BTC': {
#         'name': 'BTC',
#         'investment': '2330.55',
#         'doi': '2025-10-4',
#         '30day': '3047.44'
#     }
# }
# L2.print_investment(test['BTC'])

# sol = C.get_30day_percent('SOL')
# print(sol)
# ------------------------------------------------------------------------------

# test memory retrieval

# f = MR.getJson('app_name')
# f = L2.load_memory('app_name')
# print(f)
# ------------------------------------------------------------------------------
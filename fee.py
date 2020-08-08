#!python3
# Returns the price diff needed to cover for exchange fees given a certain purchase volume. 

import sys

EXCHANGE_FEE = 95 # price fee for GMO click s.

# Usage----
# fee.py stock_purchase_volume
#Assumes stock_purchase_volume is an int; Obviously cleaner input validations should be required for a serious tool. 
if len(sys.argv)>1:
    stock_purchase_volume = int(sys.argv[1])
    print(round(EXCHANGE_FEE/stock_purchase_volume,2))

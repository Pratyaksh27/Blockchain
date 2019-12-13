import os
import json
import ast
import csv

from blockchain import blockexplorer
from blockchain import exchangerates

##block = blockexplorer.get_block('000000000000000016f9a2c3e0f4c1245ff24856a79c34806969f5084f410680')

def get_total_transacted_value(block_id):
    total_value=0
    block = blockexplorer.get_block(block_id)
    for tx in block.transactions:
        for op in tx.outputs:
            total_value += op.value
    print('total transaction is ',total_value/pow(10,-8), ' BTC')
    return total_value

def get_foreign_exchange_rate(from_currency, to_currency):
    ticker_list = exchangerates.get_ticker()
    from_currency_last = 0.0
    to_currency_last = 0.0
    for ticker in ticker_list:
        if ticker==from_currency:
            from_currency_last = ticker_list[ticker].last
        elif ticker == to_currency:
            to_currency_last = ticker_list[ticker].last
    print(' Last Price for ',from_currency, ' is ',from_currency_last)
    print(' Last Price for ', to_currency, ' is ',to_currency_last)
    print(' 1 ',from_currency,' = ', to_currency_last/from_currency_last, ' ',to_currency)
    
    


def main():
    ret = get_total_transacted_value('000000000000000016f9a2c3e0f4c1245ff24856a79c34806969f5084f410680')
    get_foreign_exchange_rate("USD","JPY")


if __name__=='__main__':
    main()

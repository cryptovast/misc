import ccxt


def create_exchange(exchange_id):
    exchange = None
    if exchange_id == 'ftx':
        exchange = ccxt.ftx({
            'enableRateLimit': True,
            'rateLimit': 2000,
            'timeout': 30000,
        })
    return exchange


if __name__ == '__main__':
    # Very simple script that retrieves al perp markets from FTX and saves them in a txt file that you can import into
    # TV watchlist
    ftx_exchange = create_exchange(exchange_id='ftx')
    ftx_exchange.load_markets()
    with open(file='/tmp/ftx_perp_watchlist.txt', mode='w') as ftx_perp_list_file:
        for symbol in ftx_exchange.markets:
            if 'PERP' in symbol:
                ftx_perp_list_file.write(symbol.replace('-', '')+'\n')

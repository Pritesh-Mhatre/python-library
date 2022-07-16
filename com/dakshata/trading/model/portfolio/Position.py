# -*- coding: utf-8 -*-
"""
Represents a position object.
"""

class Position:

    def __init__(self, id, buyQuantity, sellQuantity, netQuantity, \
        type, pnl, mtm, buyValue, sellValue, netValue, \
        buyAvgPrice, sellAvgPrice, pseudoAccount, tradingAccount, \
        stockBroker, exchange, symbol, \
        independentExchange, independentSymbol, atPnl):
        
        self.id = id        
        self.buy_quantity = buyQuantity
        self.sell_quantity = sellQuantity
        self.net_quantity = netQuantity
        self.type = type
        self.pnl = pnl
        self.mtm = mtm
        self.buy_value = buyValue
        self.sell_value = sellValue
        self.net_value = netValue
        self.buy_avg_price = buyAvgPrice
        self.sell_avg_price = sellAvgPrice
        self.pseudo_account = pseudoAccount
        self.trading_account = tradingAccount
        self.stock_broker = stockBroker
        self.exchange = exchange
        self.symbol = symbol
        self.independent_exchange = independentExchange
        self.independent_symbol = independentSymbol
        self.atPnl = atPnl

    def __str__(self):
        return "Position[{0},{1},{2},{3},{4},Net Qty={5},Pnl={6},M2m={7},AtPnl={8}]".format( \
            self.pseudo_account, self.trading_account, self.type, \
            self.independent_exchange, self.independent_symbol, self.net_quantity, \
            self.pnl, self.mtm, self.atPnl)

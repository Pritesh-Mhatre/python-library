# -*- coding: utf-8 -*-
"""
Represents a position object.
"""

from com.dakshata.trading.model.portfolio.Position import Position

class PlatformPosition(Position):

    def __init__(self, id, buyQuantity, sellQuantity, netQuantity, \
        type, pnl, mtm, buyValue, sellValue, netValue, \
        buyAvgPrice, sellAvgPrice, pseudoAccount, tradingAccount, \
        stockBroker, exchange, symbol, \
        independentExchange, independentSymbol, \
        category, ltp, platform, accountId, overnightQuantity, \
        multiplier, realisedPnl, unrealisedPnl, state, direction, \
        atPnl, \
        *args, **kwargs):

        super().__init__(id, buyQuantity, sellQuantity, netQuantity, \
            type, pnl, mtm, buyValue, sellValue, netValue, \
            buyAvgPrice, sellAvgPrice, pseudoAccount, tradingAccount, \
            stockBroker, exchange, symbol, \
            independentExchange, independentSymbol, atPnl)
    
        self.category = category
        self.ltp = ltp
        self.platform = platform
        self.account_id = accountId
        self.overnight_quantity = overnightQuantity
        self.multiplier = multiplier
        self.realised_pnl = realisedPnl
        self.unrealised_pnl = unrealisedPnl
        self.state = state
        self.direction = direction

    def __str__(self):
        return super().__str__()
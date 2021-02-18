# -*- coding: utf-8 -*-
"""
Represents a order object.
"""

class PlatformHolding:

    def __init__(self, id, isin, collateralType, instrumentToken, \
        product, quantity, collateralQty, t1Qty, pnl, haircut, \
        avgPrice, pseudoAccount, tradingAccount, \
        stockBroker, exchange, symbol, \
        platform, *args, **kwargs):
    
        self.id = id
        self.isin = isin
        self.collateral_type = collateralType
        self.instrument_token = instrumentToken
        self.product = product
        self.quantity = quantity
        self.collateral_qty = collateralQty
        self.t1_qty = t1Qty
        self.pnl = pnl
        self.haircut = haircut
        self.avg_price = avgPrice
        self.pseudo_account = pseudoAccount
        self.trading_account = tradingAccount
        self.stock_broker = stockBroker
        self.exchange = exchange
        self.symbol = symbol
        self.platform = platform

    def __str__(self):
        return ("Margin[Pseudo Acc: {0}, Trading Acc: {1}, Broker: {2}, "
            "Exchange: {3}, Symbol: {4}, Quantity: {5}, Inst. Token: {6}]").format( \
            self.pseudo_account, self.trading_account, self.stock_broker, \
            self.exchange, self.symbol, self.quantity, self.instrument_token)

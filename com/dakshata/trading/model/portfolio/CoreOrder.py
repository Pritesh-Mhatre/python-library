# -*- coding: utf-8 -*-
"""
Represents an order object.
"""

class CoreOrder:

    def __init__(self, id, tradeType, orderType, productType, \
        variety, validity, quantity, disclosedQuantity, \
        price, triggerPrice, amo, statusMessage, publisherId, \
        pseudoAccount, tradingAccount, stockBroker, exchange, symbol, \
        independentExchange, independentSymbol, \
        modifiedTime, createdTime):
        
        self.id = id
        self.trade_type = tradeType
        self.order_type = orderType
        self.product_type = productType
        self.variety = variety
        self.validity = validity
        self.quantity = quantity
        self.disclosed_quantity = disclosedQuantity
        self.price = price
        self.trigger_price = triggerPrice
        self.amo = amo
        self.status_message = statusMessage
        self.publisher_id = publisherId
        self.pseudo_account = pseudoAccount
        self.trading_account = tradingAccount
        self.stock_broker = stockBroker
        self.exchange = exchange
        self.symbol = symbol
        self.independent_exchange = independentExchange
        self.independent_symbol = independentSymbol
        self.modified_time = modifiedTime
        self.modified_time = createdTime

    def __str__(self):
        return "Order[{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}]".format( \
            self.pseudo_account, self.variety, self.independent_exchange, \
            self.independent_symbol, self.product_type, self.trade_type, \
            self.order_type, self.quantity, self.price, self.trigger_price, self.id)

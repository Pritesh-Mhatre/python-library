# -*- coding: utf-8 -*-
"""
Represents a order object.
"""

from com.dakshata.trading.model.portfolio.CoreOrder import CoreOrder

class PlatformOrder(CoreOrder):

    def __init__(self, id, tradeType, orderType, productType, \
        variety, validity, quantity, disclosedQuantity, \
        price, triggerPrice, amo, statusMessage, publisherId, \
        pseudoAccount, tradingAccount, stockBroker, exchange, symbol, \
        independentExchange, independentSymbol, \
        modifiedTime, createdTime, \
        parentOrderId, exchangeOrderId, averagePrice, \
        clientId, rawStatus, platformTime, exchangeTime, \
        pendingQuantity, filledQuantity, platform, \
        status, nestRequestId, *args, **kwargs):
        
        super().__init__(id, tradeType, orderType, productType, \
            variety, validity, quantity, disclosedQuantity, \
            price, triggerPrice, amo, statusMessage, publisherId, \
            pseudoAccount, tradingAccount, stockBroker, exchange, symbol, \
            independentExchange, independentSymbol, \
            modifiedTime, createdTime)
        
        self.parent_order_id = parentOrderId
        self.exchange_order_id = exchangeOrderId
        self.average_price = averagePrice
        self.client_id = clientId
        self.raw_status = rawStatus
        self.platform_time = platformTime
        self.exchange_time = exchangeTime
        self.pending_quantity = pendingQuantity
        self.filled_quantity = filledQuantity
        self.platform = platform
        self.status = status
        self.nest_request_id = nestRequestId

    def is_open(self):
        return this.status and this.status.upper() == 'OPEN'

    def is_trigger_pending(self):
        return this.status and this.status.upper() == 'TRIGGER_PENDING'

    def is_open_or_trigger_pending(self):
        return self.is_open() or self.is_trigger_pending()

    def is_cancelled(self):
        return this.status and this.status.upper() == 'CANCELLED'

    def is_rejected(self):
        return this.status and this.status.upper() == 'REJECTED'

    def __str__(self):
        return super().__str__()
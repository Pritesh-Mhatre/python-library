# -*- coding: utf-8 -*-
"""
Main class which provides all of AutoTrader Web's API functions.

Use the createInstance() method to create an instance of this class.
You can then re-use this instance throughout your application.
There is no need to recreate the instance multiple times.
"""

import requests

from com.dakshata.data.model.common.OperationResponse import OperationResponse

class AutoTrader:

    __TRADING_URI = "/trading"

    __ACCOUNT_URI = "/account"

    __instances = {}

    @staticmethod 
    def create_instance(api_key, service_url):
        """
        Creates an instance of AutoTrader class or returns an existing instance.
        This factory method makes sure to have only one instance 
        of the AutoTrader class per api_key.

        Keyword arguments:
        api_key -- API key used for authentication (you can find it in AutoTrader settings)
        service_url -- the url of AutoTrader Web's (see API docs)
        """

        a = AutoTrader.__instances.get(api_key, None)
        if a != None:
            return a
        else:
            return AutoTrader(api_key, service_url)

    def __init__(self, api_key, service_url):
        """
        Supposed to be a private constructor, so do not use it directly.

        Keyword arguments:
        api_key -- API key used for authentication (you can find it in AutoTrader settings)
        service_url -- the url of AutoTrader Web's (see API docs)
        """

        a = AutoTrader.__instances.get(api_key, None)
        if a != None:
            raise Exception("Please use create_instance() method!")
        else:
            self.api_key = api_key
            self.service_url = service_url
            AutoTrader.__instances[api_key] = self

    def __post(self, uri, data):
        """
        Private method to post data to the server.
        """
        url = self.service_url + uri
        headers = {'api-key': self.api_key}

        request = requests.post(url, headers=headers, data=data)
        response = request.json()
        result = OperationResponse(**response)

        return result

    def __cancel_order(self, uri, pseudoAccount, platform_id):
        """
        Private method to cancel an order.
        """

        data = {'pseudoAccount': pseudoAccount, \
            'platformId': platform_id}

        return self.__post(uri, data)

    def cancel_order_by_platform_id(self, pseudoAccount, platform_id):
        """
        Cancels an open order (see API docs).

        https://stocksdeveloper.in/documentation/api/cancel-order/
        """

        return self.__cancel_order("/cancelOrderByPlatformId", pseudoAccount, platform_id)

    def cancel_child_orders_by_platform_id(self, pseudoAccount, platform_id):
        """
        This API function is useful for exiting from an open bracket or cover order position (see API docs).

        https://stocksdeveloper.in/documentation/api/cancel-child-orders/
        """

        return self.__cancel_order("/cancelChildOrdersByPlatformId", pseudoAccount, platform_id)

    def place_regular_order(self, pseudoAccount, \
            exchange, symbol, tradeType, orderType, \
            productType, quantity, price, triggerPrice=0.0):
        """
        Places a regular order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-regular-order/
        """

        data = {'pseudoAccount': pseudoAccount, \
            'exchange': exchange, \
            'symbol': symbol, \
            'tradeType': tradeType, \
            'orderType': orderType, \
            'productType': productType, \
            'quantity': quantity, \
            'price': price,
            'triggerPrice': triggerPrice}

        return self.__post("/placeRegularOrder", data)

    def place_bracket_order(self, pseudoAccount, \
            exchange, symbol, tradeType, orderType, \
            quantity, price, triggerPrice,
            target, stoploss, trailingStoploss=0.0):
        """
        Places a bracket order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-bracket-order/
        """

        data = {'pseudoAccount': pseudoAccount, \
            'exchange': exchange, \
            'symbol': symbol, \
            'tradeType': tradeType, \
            'orderType': orderType, \
            'quantity': quantity, \
            'price': price,
            'triggerPrice': triggerPrice,
            'target': target,
            'stoploss': stoploss,
            'trailingStoploss': trailingStoploss}

        return self.__post("/placeBracketOrder", data)            

    def place_cover_order(self, pseudoAccount, \
            exchange, symbol, tradeType, orderType, \
            productType, quantity, price, triggerPrice):
        """
        Places a cover order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-cover-order/
        """

        data = {'pseudoAccount': pseudoAccount, \
            'exchange': exchange, \
            'symbol': symbol, \
            'tradeType': tradeType, \
            'orderType': orderType, \
            'quantity': quantity, \
            'price': price,
            'triggerPrice': triggerPrice}

        return self.__post("/placeCoverOrder", data)


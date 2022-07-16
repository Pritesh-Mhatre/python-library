# -*- coding: utf-8 -*-
"""
Main class which provides all of AutoTrader Web's API functions.

Use the create_instance() method to create an instance of this class.
You can then re-use this instance throughout your application.
There is no need to recreate the instance multiple times.
"""

import sys
import requests

from json import JSONDecodeError

from com.dakshata.data.model.common.OperationResponse import OperationResponse
from com.dakshata.trading.model.platform.PlatformMargin import PlatformMargin
from com.dakshata.trading.model.platform.PlatformOrder import PlatformOrder
from com.dakshata.trading.model.platform.PlatformPosition import PlatformPosition
from com.dakshata.trading.model.platform.PlatformHolding import PlatformHolding

class AutoTrader:

    __TRADING_URI = "/trading"

    __ACCOUNT_URI = "/account"

    __instances = {}
    
    PRIMARY_SERVER_URL = "https://apix.stocksdeveloper.in"
    
    BACKUP_SERVER_URL = "https://api.stocksdeveloper.in"
    
    SERVER_URL = PRIMARY_SERVER_URL

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
        if a:
            raise Exception("Please use create_instance() method!")
        else:
            self.api_key = api_key
            self.service_url = service_url
            AutoTrader.__instances[api_key] = self

    def __request(self, uri, data, request_lambda):
        """
        Private method to post data to the server.
        """
        url = self.service_url + AutoTrader.__TRADING_URI + uri
        headers = {'api-key': self.api_key}

        try:
            # Execute the request
            response = request_lambda(url, headers, data)
            
            # Check for success
            if(response.ok):
                try:
                    # Convert response to JSON
                    jsonResponse = response.json()
                    # Raise JSON conversion error
                    response.raise_for_status()
                    # Convert the JSON to python OperationResponse object
                    result = OperationResponse(**jsonResponse)
                    return result                    
                except JSONDecodeError:
                    print("ERROR: Failure while converting response to JSON.")
                    print(response)
                    raise
                
            else:
                # A forbidden error is thrown when authentication fails
                if(response.status_code == requests.codes.forbidden):
                    message = "ERROR: Either your API Key is wrong or the user might be disabled."
                    print(message)
                    raise Exception(message)
                else:
                    response.raise_for_status()
            
        except:
            print("ERROR: Unexpected error:", sys.exc_info()[0])
            raise
    
    def __get(self, pseudo_account, uri):
        """
        Private method to post data to the server.
        """
        data = {'pseudoAccount': pseudo_account}
        
        return self.__request(uri, data, lambda u, h, d: requests.get(u, headers=h, params=d))

    def __post(self, uri, data):
        """
        Private method to post data to the server.
        """
        return self.__request(uri, data, lambda u, h, d: requests.post(u, headers=h, data=d))

    def __cancel_order(self, uri, pseudo_account, platform_id=None):
        """
        Private method to cancel an order.
        """

        data = {'pseudoAccount': pseudo_account}

        if platform_id:
            data['platformId'] = platform_id

        return self.__post(uri, data)

    def cancel_all_orders(self, pseudo_account):
        """
        Cancels all open orders from a given account (see API docs).

        https://stocksdeveloper.in/documentation/api/cancel-all-orders/
        """

        return self.__cancel_order("/cancelAllOrders", pseudo_account)

    def cancel_order_by_platform_id(self, pseudo_account, platform_id):
        """
        Cancels an open order (see API docs).

        https://stocksdeveloper.in/documentation/api/cancel-order/
        """

        return self.__cancel_order("/cancelOrderByPlatformId", pseudo_account, platform_id)

    def cancel_child_orders_by_platform_id(self, pseudo_account, platform_id):
        """
        This API function is useful for exiting from an open bracket or cover order position (see API docs).

        https://stocksdeveloper.in/documentation/api/cancel-child-orders/
        """

        return self.__cancel_order("/cancelChildOrdersByPlatformId", pseudo_account, platform_id)

    def modify_order_by_platform_id(self, pseudo_account, platform_id, \
        order_type=None, quantity=None, price=None, trigger_price=None):
        """
        Modifies an open order’s attributes like order type, quantity, price & trigger price (see API docs).
        Pass only those parameters that you need to modify.

        https://stocksdeveloper.in/documentation/api/modify-order/
        """
        data = {'pseudoAccount': pseudo_account, \
            'platformId': platform_id}
        
        if order_type:
            data['orderType'] = order_type
        if quantity:
            data['quantity'] = quantity
        if price:
            data['price'] = price
        if trigger_price:
            data['triggerPrice'] = trigger_price

        return self.__post("/modifyOrderByPlatformId", data)

    def place_regular_order(self, pseudo_account,
            exchange, symbol, tradeType, orderType,
            productType, quantity, price, triggerPrice=0.0):
        """
        Places a regular order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-regular-order/
        """

        data = {'pseudoAccount': pseudo_account,
            'exchange': exchange,
            'symbol': symbol,
            'tradeType': tradeType,
            'orderType': orderType,
            'productType': productType,
            'quantity': quantity,
            'price': price,
            'triggerPrice': triggerPrice}

        return self.__post("/placeRegularOrder", data)

    def place_bracket_order(self, pseudo_account,
            exchange, symbol, tradeType, orderType,
            quantity, price, triggerPrice,
            target, stoploss, trailingStoploss=0.0):
        """
        Places a bracket order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-bracket-order/
        """

        data = {'pseudoAccount': pseudo_account,
            'exchange': exchange,
            'symbol': symbol,
            'tradeType': tradeType,
            'orderType': orderType,
            'quantity': quantity,
            'price': price,
            'triggerPrice': triggerPrice,
            'target': target,
            'stoploss': stoploss,
            'trailingStoploss': trailingStoploss}

        return self.__post("/placeBracketOrder", data)            

    def place_cover_order(self, pseudo_account,
            exchange, symbol, tradeType, orderType,
            quantity, price, triggerPrice):
        """
        Places a cover order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-cover-order/
        """

        data = {'pseudoAccount': pseudo_account,
            'exchange': exchange,
            'symbol': symbol,
            'tradeType': tradeType,
            'orderType': orderType,
            'quantity': quantity,
            'price': price,
            'triggerPrice': triggerPrice}

        return self.__post("/placeCoverOrder", data)

    def place_advanced_order(self, variety, pseudo_account,
            exchange, symbol, tradeType, orderType,
            productType, quantity, price, triggerPrice,
            target, stoploss, trailingStoploss,
            disclosedQuantity, validity, amo,
            strategyId, comments, publisherId):
        """
        Places an advanced order (see API docs).

        https://stocksdeveloper.in/documentation/api/place-advanced-order/
        """

        data = {'variety': variety,
            'pseudoAccount': pseudo_account,
            'exchange': exchange,
            'symbol': symbol,
            'tradeType': tradeType,
            'orderType': orderType,
            'productType': productType,
            'quantity': quantity,
            'price': price,
            'triggerPrice': triggerPrice,
            'target': target,
            'stoploss': stoploss,
            'trailingStoploss': trailingStoploss,
            'disclosedQuantity': disclosedQuantity,
            'validity': validity,
            'amo': amo,
            'strategyId': strategyId,
            'comments': comments,
            'publisherId': publisherId}

        return self.__post("/placeAdvancedOrder", data)

    def square_off_position(self, pseudo_account, \
        position_category, position_type, exchange, symbol):
        """
        API function to square-off a position (see API docs).

        https://stocksdeveloper.in/documentation/api/square-off-position/
        """

        data = {'pseudoAccount': pseudo_account, \
            'category': position_category, \
            'type': position_type, \
            'exchange': exchange, \
            'symbol': symbol}

        return self.__post("/squareOffPosition", data)

    def square_off_portfolio(self, pseudo_account, position_category):
        """
        API function to square-off portfolio or account (see API docs).

        https://stocksdeveloper.in/documentation/api/square-off-portfolio/
        """

        data = {'pseudoAccount': pseudo_account, \
            'category': position_category}

        return self.__post("/squareOffPortfolio", data)

    def read_platform_margins(self, pseudo_account):
        """
        API function to read margins from your trading platform (see API docs).

        https://stocksdeveloper.in/documentation/api/read-margins/
        """

        response = self.__get(pseudo_account, "/readPlatformMargins")
        
        if response.result and isinstance(response.result, list):
            margins = []
            for m in response.result:
                margins.append(PlatformMargin(**m))
            response.result = margins
        
        return response

    def read_platform_orders(self, pseudo_account):
        """
        API function to read orders from your trading platform (see API docs).

        https://stocksdeveloper.in/documentation/api/read-orders/
        """

        response = self.__get(pseudo_account, "/readPlatformOrders")
        
        if response.result and isinstance(response.result, list):
            orders = []
            for m in response.result:
                orders.append(PlatformOrder(**m))
            response.result = orders
        
        return response

    def read_platform_positions(self, pseudo_account):
        """
        API function to read positions from your trading platform (see API docs).

        https://stocksdeveloper.in/documentation/api/read-positions/
        """

        response = self.__get(pseudo_account, "/readPlatformPositions")
        
        if response.result and isinstance(response.result, list):
            positions = []
            for m in response.result:
                positions.append(PlatformPosition(**m))
            response.result = positions
        
        return response

    def read_platform_holdings(self, pseudo_account):
        """
        API function to read positions from your trading platform (see API docs).

        https://stocksdeveloper.in/documentation/api/read-holdings/
        """

        response = self.__get(pseudo_account, "/readPlatformHoldings")
        
        if response.result and isinstance(response.result, list):
            holdings = []
            for m in response.result:
                holdings.append(PlatformHolding(**m))
            response.result = holdings
        
        return response

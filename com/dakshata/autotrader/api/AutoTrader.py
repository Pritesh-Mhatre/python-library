# -*- coding: utf-8 -*-
"""Main class which provides all of AutoTrader Web's API functions.

Use the createInstance() method to create an instance of this class.
You can then re-use this instance throughout your application.
There is no need to recreate the instance multiple times.
"""

import requests

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
        
    def execute(self, uri, data):
        """
        Executes an API request.
        """

        url = self.service_url + uri
        headers = {'api-key': self.api_key}
        r = requests.post(url, headers=headers, data=data)
        
        return r
        
    def place_regular_order(self, pseudoAccount, \
            exchange, symbol, tradeType, orderType, \
            productType, quantity, price, triggerPrice=0.0):
        """
        Places a regular order (see API docs).
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
        
        return self.execute(AutoTrader.__TRADING_URI + "/placeRegularOrder", data)
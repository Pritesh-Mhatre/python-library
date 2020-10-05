class AutoTrader:
    
    __instances = {}
    
    @staticmethod 
    def createInstance(apiKey, serviceUrl):
        a = AutoTrader.__instances.get(apiKey, None)
        if a != None:
            return a
        else:
            return AutoTrader(apiKey, serviceUrl)
    
    def __init__(self, apiKey, serviceUrl):
        a = AutoTrader.__instances.get(apiKey, None)
        if a != None:
            raise Exception("Please use createInstance() method!")
        else:
            self.apiKey = apiKey
            self.serviceUrl = serviceUrl
            AutoTrader.__instances[apiKey] = self
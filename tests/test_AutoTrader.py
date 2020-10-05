import unittest

from com.dakshata.autotrader.api.AutoTrader import AutoTrader

class TestAutoTrader(unittest.TestCase):

    __PROD_SERVER = 'https://stocksdeveloper.in:9017/'
    
    __TEST_SERVER = 'http://localhost:9017'

    def test_place_regular_order(self):
        """
        Test that it can sum a list of integers
        """
        api = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        
        result = api.place_regular_order('159401', 'NSE', 'WIPRO', 'BUY', 'LIMIT', 'INTRADAY', 10, 330.35, 0.0)
        
        self.assertTrue(result.success())
        
        self.assertIsNotNone(result.result)
        
        self.assertNotEqual('', result.result)
        
if __name__ == '__main__':
    unittest.main()
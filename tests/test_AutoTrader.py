import unittest

from com.dakshata.autotrader.api.AutoTrader import AutoTrader

class TestAutoTrader(unittest.TestCase):

    __PROD_SERVER = 'https://stocksdeveloper.in:9017/'
    
    __TEST_SERVER = 'http://localhost:9017'
    
    __API = None

    @classmethod
    def setUpClass(cls):
        TestAutoTrader.__API = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        
    def test_place_regular_order(self):
        """
        Test placing a regular order.
        """
        response = TestAutoTrader.__API.place_regular_order( \
            '159401', 'NSE', 'WIPRO', 'BUY', 'LIMIT', 'INTRADAY', 1, 330.35, 0.0)
        
        # print(result)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertNotEqual('', response.result)

    def test_place_bracket_order(self):
        """
        Test placing a bracket order.
        """
        response = TestAutoTrader.__API.place_bracket_order( \
            '159401', 'NSE', 'WIPRO', 'SELL', 'LIMIT', 1, 326.35, 0.0, 1, 1, 0)
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertNotEqual('', response.result)

    def test_place_cover_order(self):
        """
        Test placing a cover order.
        """
        response = TestAutoTrader.__API.place_cover_order( \
            '159401', 'NSE', 'SBIN', 'SELL', 'LIMIT', 1, 188.15, 190.0)
        
        # print(response)
        
        self.assertTrue(response.success())        
        self.assertIsNotNone(response.result)
        self.assertNotEqual('', response.result)
        
    def test_read_platform_margins(self):
        """
        Test reading margins data.
        """        
        response = TestAutoTrader.__API.read_platform_margins('159401')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertIsInstance(response.result, list)        
        
        # print(*response.result, sep = "\n\n")
        
    def test_read_platform_orders(self):
        """
        Test reading orders data.
        """        
        response = TestAutoTrader.__API.read_platform_orders('159401')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertIsInstance(response.result, list)        
        
        print(*response.result, sep = "\n\n")
        
    def test_read_platform_positions(self):
        """
        Test reading positions data.
        """        
        response = TestAutoTrader.__API.read_platform_positions('159401')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertIsInstance(response.result, list)        
        
        print(*response.result, sep = "\n\n")
    
if __name__ == '__main__':
    unittest.main()
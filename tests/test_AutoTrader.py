import unittest

from com.dakshata.autotrader.api.AutoTrader import AutoTrader

class TestAutoTrader(unittest.TestCase):
    
    __TEST_SERVER = 'http://localhost:9017'
    
    __API = None

    @classmethod
    def setUpClass(cls):
        #TestAutoTrader.__API = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        TestAutoTrader.__API = AutoTrader.create_instance('<api-key>', AutoTrader.SERVER_URL)
        
    def test_place_regular_order(self):
        """
        Test placing a regular order.
        """
        response = TestAutoTrader.__API.place_regular_order( \
            '159401', 'NSE', 'WIPRO', 'BUY', 'LIMIT', 'INTRADAY', 1, 330.35, 0.0)
        
        # print(response)
        
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
        
    def test_cancel_order_by_platform_id(self):
        """
        Test cancel order.
        """        
        response = TestAutoTrader.__API.cancel_order_by_platform_id('159401', '201026000614309')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)        
        
    def test_cancel_child_orders_by_platform_id(self):
        """
        Test exit BO or CO order.
        """        
        response = TestAutoTrader.__API.cancel_child_orders_by_platform_id('159401', '201007000448051')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)        
        
    def test_cancel_all_orders(self):
        """
        Test cancel all order.
        """        
        response = TestAutoTrader.__API.cancel_all_orders('159401')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)        
        
    def test_modify_order_by_platform_id(self):
        """
        Test modify order.
        """        
        response = TestAutoTrader.__API.modify_order_by_platform_id('159401', '201007000443194', price=325.9)
        # response = TestAutoTrader.__API.modify_order_by_platform_id('159401', '201007000443194', quantity=2)
        # response = TestAutoTrader.__API.modify_order_by_platform_id('159401', '201007000443194', trigger_price=322)
        # response = TestAutoTrader.__API.modify_order_by_platform_id('159401', '201007000443194', order_type='MARKET')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)        
        
    def test_square_off_position(self):
        """
        Test square-off position.
        """        
        response = TestAutoTrader.__API.square_off_position('159401', 'DAY', 'MIS', 'NSE', 'WIPRO')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)        
        
        
    def test_square_off_portfolio(self):
        """
        Test square-off portfolio.
        """        
        response = TestAutoTrader.__API.square_off_portfolio('159401', 'DAY')
        
        print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)        
        
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
        
        # print(*response.result, sep = "\n\n")
        
    def test_read_platform_positions(self):
        """
        Test reading positions data.
        """        
        response = TestAutoTrader.__API.read_platform_positions('159401')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertIsInstance(response.result, list)        
        
        # print(*response.result, sep = "\n\n")
    
if __name__ == '__main__':
    unittest.main()
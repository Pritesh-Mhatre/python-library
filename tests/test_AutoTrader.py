import unittest

from com.dakshata.autotrader.api.AutoTrader import AutoTrader

# How to run?
# 1. Add your API Key below in the placeholder
# 2. From project home directory, run following command.
#       python -m unittest tests.test_AutoTrader.TestAutoTrader.test_read_platform_orders
#       Note: Write the name of the desired test case
class TestAutoTrader(unittest.TestCase):
    
    __TEST_SERVER = 'http://localhost:9017'
    
    __API = None

    @classmethod
    def setUpClass(cls):
        TestAutoTrader.__API = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        #TestAutoTrader.__API = AutoTrader.create_instance('<api-key>', AutoTrader.SERVER_URL)
        
    def printMargins(self, margins):
        for o in margins:
            pretty = "[Pseudo acc.: {}, Trading acc.: {}, Category: {}, Funds: {}, " + \
                "Utilized: {}, Available: {}, Total: {}, Net: {}, Span: {}, " + \
                "Exposure: {}, Collateral: {}, Payin: {}, Payout: {}, Adhoc: {}, " + \
                "Real. Mtm: {}, Unreal. Mtm: {}, Broker: {}, ]"
            print(pretty.format(o.pseudo_account, o.trading_account, o.category,
                o.funds, o.utilized, o.available, o.total, o.net, o.span, o.exposure, 
                o.collateral, o.payin, o.payout, o.adhoc, o.realised_mtm, 
                o.unrealised_mtm, o.stock_broker))
            print("\n----------------------------------------------------------------------\n")
        
    def printOrders(self, orders):
        for o in orders:
            pretty = "[Pseudo acc.: {}, Trading acc.: {}, Ind. exch: {}, Ind. symbol: {}, " + \
                "Id: {}, Variety: {}, Trade type: {}, Order type: {}, Product type: {}, " + \
                "Quantity: {}, Price: {}, Trigger price: {}, Status: {}, Pending qty.: {}, " + \
                "Filled qty.: {}, Broker: {}, Platform: {}]"
            print(pretty.format(o.pseudo_account, o.trading_account, o.independent_exchange, 
                o.independent_symbol, o.id, o.variety, o.trade_type, o.order_type, o.product_type, 
                o.quantity, o.price, o.trigger_price, o.status, o.pending_quantity, o.filled_quantity, 
                o.stock_broker, o.platform))
            print("\n----------------------------------------------------------------------\n")
        
    def printPositions(self, positions):
        for o in positions:
            pretty = "[Category: {}, Type: {}, Pseudo acc.: {}, Trading acc.: {}, " + \
                "Ind. exch: {}, Ind. symbol: {}, Pnl: {}, Mtm: {}, Net qty.: {}, " + \
                "Buy qty.: {}, Sell qty.: {}, Net value: {}, Buy value: {}, Sell value: {}, " + \
                "Buy avg. price: {}, Sell avg. price: {}, Realised pnl: {}, " + \
                "Unrealised pnl: {}, Broker: {}, Platform: {}]"
            print(pretty.format(o.category, o.type, o.pseudo_account, o.trading_account, 
                o.independent_exchange, o.independent_symbol, o.pnl, o.mtm, o.net_quantity, 
                o.buy_quantity, o.sell_quantity, o.net_value, o.buy_value, o.sell_value, 
                o.buy_avg_price, o.sell_avg_price, o.realised_pnl, o.unrealised_pnl,
                o.stock_broker, o.platform))
            print("\n----------------------------------------------------------------------\n")
        
    def printHoldings(self, holdings):
        for o in holdings:
            pretty = "[Pseudo acc.: {}, Trading acc.: {}, " + \
                "Exch: {}, Symbol: {}, Quantity: {}, Product: {}, ISIN: {}, " + \
                "Collateral qty.: {}, T1 qty.: {}, Collateral type: {}, Pnl: {}, Haircut: {}, " + \
                "Avg. price: {}, Inst. token: {}]"
            print(pretty.format(o.pseudo_account, o.trading_account, 
                o.exchange, o.symbol, o.quantity, o.product, o.isin, 
                o.collateral_qty, o.t1_qty, o.collateral_type, o.pnl, o.haircut, 
                o.avg_price, o.instrument_token))
            print("\n----------------------------------------------------------------------\n")
        
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
        
    def test_place_advanced_order(self):
        """
        Test placing an advanced order.
        """
        response = TestAutoTrader.__API.place_advanced_order( \
            'REGULAR', '159401', 'NSE', 'SBIN', 'SELL', 'LIMIT', 'INTRADAY', \
            1, 410.35, 0.0, 0.0, 0.0, 0.0, 0, 'DAY', False, '', '', '')
        
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
        self.printMargins(response.result)
        
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
        
        self.printOrders(response.result)
        
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
        
        self.printPositions(response.result)
    
    def test_read_platform_holdings(self):
        """
        Test reading holdings data.
        """        
        response = TestAutoTrader.__API.read_platform_holdings('159401')
        
        # print(response)
        
        self.assertTrue(response.success())
        self.assertIsNotNone(response.result)
        self.assertIsInstance(response.result, list)        
        
        # print(*response.result, sep = "\n\n")
        
        self.printHoldings(response.result)
    
if __name__ == '__main__':
    unittest.main()
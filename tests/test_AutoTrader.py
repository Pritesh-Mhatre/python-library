import unittest

from com.dakshata.autotrader.api.AutoTrader import AutoTrader

class TesAutoTrader(unittest.TestCase):
    def test_place_regular_order(self):
        """
        Test that it can sum a list of integers
        """
        api = AutoTrader.create_instance('4586c256-b284-4a4c-9bd4-88f1ffed1755', 'https://stocksdeveloper.in:9017/')
        
        response = api.place_regular_order('159401', 'NSE', 'WIPRO', 'BUY', 'LIMIT', 'INTRADAY', 330.35, 0.0)
        
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
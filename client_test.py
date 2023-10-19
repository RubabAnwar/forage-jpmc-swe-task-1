import unittest
from client3 import getDataPoint, getRatio, quotes


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
  for quote in quotes:
    result = getDataPoint(quote)
    self.assertEqual(result, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  for quote in quotes:
    result = getDataPoint(quote)
    self.assertEqual(result, (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_nonzeroPriceB(self):
    price_a = 10
    price_b = 5
    result = getRatio(price_a, price_b)
    self.assertEqual(result, 2)

  def test_getRatio_zeroPriceB(self):
    price_a = 10
    price_b = 0
    result = getRatio(price_a, price_b)
    self.assertIsNone(result)

  def test_getRatio_zeroPriceA(self):
    price_a = 0
    price_b = 5
    result = getRatio(price_a, price_b)
    self.assertEqual(result, 0)

  def test_getRatio_samePrices(self):
    price_a = 10
    price_b = 10
    result = getRatio(price_a, price_b)
    self.assertEqual(result, 1)


if __name__ == '__main__':
  unittest.main()
import unittest
from unittest import TestCase
from papka.main import *

class TestOne(TestCase):
    def test_best_web(self):
        result = better_web(stats)
        better = 'yandex'
        self.assertEqual(result,better)

    def test_correct(self):
        result = my_list(ids)
        numerical_order = [98, 35, 213, 54, 119, 15]
        assert result == numerical_order

    def test_geo(self):
        result = geo(geo_logs)
        list_geo = ['Москва', 'Владимир', 'Тула', 'Тула', 'Курск', 'Архангельск']
        assert result == list_geo

    def test_ya(self):
        result = get_foldres()
        finish_geo_log = 201
        assert result == finish_geo_log 


if __name__ == '__main__':
    unittest.main()
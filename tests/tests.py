import unittest

from bs4 import BeautifulSoup
import os

from libbvl import utilitarios


class TestUtilitarios(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        with open(dir + "/estados_financieros.html", "r") as handle:
            self.html_soup = BeautifulSoup(handle.read())

    def test_hallar_valor(self):
        result = utilitarios.hallar_valor(self.html_soup, "1F2001", "B")
        self.assertEqual("54,394,604", result)


if __name__ == '__main__':
    unittest.main()

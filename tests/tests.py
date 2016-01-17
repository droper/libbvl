import unittest

from bs4 import BeautifulSoup

from libbvl.utilitarios import hallar_valor


class TestUtilitarios(unittest.TestCase):
    def setUp(self):
        with open("estados_financieros.html", "r") as handle:
            self.html_soup = BeautifulSoup(handle.read())

    def test_hallar_valor(self):
        result = hallar_valor(self.html_soup, "1F2001", "B")
        self.assertEqual("54,394,604", result)

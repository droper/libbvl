#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup
from libbvl.utilitarios import find_tag, report_html, hallar_valor
from libbvl.config import URL_BALANCE_GENERAL, URL_GANANCIAS_PERDIDAS, \
GANANCIA_PERDIDA

url = URL_GANANCIAS_PERDIDAS

html = report_html(url)

report_tree = BeautifulSoup(html, "html.parser")

print hallar_valor(report_tree, '2D07ST', GANANCIA_PERDIDA)


#print report_tree.find_all('th', 'td')

#print reporte, '\n\n'

"""
for tag in reporte.descendants:
    try:
       if tag.text.count(\
           u'1D0109') > 0:
          print tag.contents[33].text#.next_sibling.next_sibling.next_sibling.text
          break
    except:
       pass
"""

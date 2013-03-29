#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup
from descarga_funciones import report_html
from utilities import find_tag

url = \
"http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano=2012&Trimestre=3&Rpj=002597&RazoSoci=SOCIEDAD%20MINERA%20CORONA%20S.A.&TipoEEFF=PAT&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

html = report_html(url)

report_tree = BeautifulSoup(html)

reporte =\
report_tree.body.center.table.contents[1].td.table.tr.contents[3].table.contents[5].td.table
print reporte, '\n\n'

print len(list(reporte.descendants))

print find_tag(reporte,u'4D0204',33)

for tag in reporte.descendants:
    try:
       if tag.text.count(\
           u'4D0204') > 0:
          print tag.contents[33].text#.next_sibling.next_sibling.next_sibling.text
          break
    except:
       pass

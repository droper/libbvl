#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup


def report_html(url):

    #Open the report url
    try:
       report = urlopen(url)
    except IOError:
       return 0

    html = report.read()
    report.close()

    report_tree = BeautifulSoup(html)

    #Si no existe la url, el server devolvera la pantalla
    #"No existe la informacion solicitada"
    #Se cuenta la cantidad de veces que se repite 'No existe' en el texto
    #error_text = report_tree.body.center.table.tr.td.table.tr.contents[3].table.contents[3].td.text.count('No existe')
    error_text = \
    find_tag(report_tree.body.center.table.tr.td.table.tr.contents[3].table, \
    'No existe', 1)

    #print error_text
    #Si hay mas de 0 'No' entonces se devuelve Falso
    if error_text:
       print "no existe url"
       return False

    return html

def find_tag(html, tag_text, tag_position):
    #If find the text in the tag, returns the requiered html element
    for tag in html.descendants:
        try:
            if tag.text.count(tag_text) > 0:
                return tag.contents[tag_position].text
        except:
            pass



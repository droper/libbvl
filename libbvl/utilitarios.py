#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Funciones utilizadas por el resto de la librería"""

from urllib2 import urlopen
from bs4 import BeautifulSoup


def report_html(url):
    """Devuelve el html del url pasado como parámetro"""

    # Open the report url
    try:
        report = urlopen(url)
    except IOError:
        return 0

    html = report.read()
    report.close()

    report_tree = BeautifulSoup(html)

    # Si no existe la url, el server devolvera la pantalla
    # "No existe la informacion solicitada"
    # Se cuenta la cantidad de veces que se repite 'No existe' en el texto
    error_text = \
    find_tag(report_tree.body.center.table.tr.td.table.tr.contents[3].table, \
    'No existe', 1)

    # Si hay mas de 0 'No' entonces se devuelve Falso
    if error_text:
        return False

    return html

def find_tag(html, tag_text, tag_position):
    """Encuentra el texto del tag buscado en el html"""

    # Si encuentra el texto en el tag, retorna el elemento html requerido
    for tag in html.descendants:
        # Se comprueba que el tag tenga el atributo text para no generar una
        # excepción AttributeError
        if hasattr(tag, 'text'):
            # Se busca el texto en el tag (en caso de tablas una fila),
            # si existe se retorna el contenido del campo indicado del tag  
            if tag.text.count(tag_text) > 0:
                return tag.contents[tag_position].text



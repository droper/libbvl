#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Funciones utilizadas por el resto de la librería"""

from urllib2 import urlopen
from bs4 import BeautifulSoup

from config import BALANCE, GANANCIA_PERDIDA, CAMBIO_PATRIMONIO, \
                   FLUJO_EFECTIVO, CONSTANT_ANHO

def report_html(url):
    """Devuelve el html del url pasado como parámetro"""

    # Open the report url
    try:
        report = urlopen(url)
    except IOError:
        return 0
    except ValueError:
        # Si url es la ruta de un archivo
        report = open(url)

    html = report.read()
    report.close()

    report_tree = BeautifulSoup(html)

    # Si no existe la url, el server devolverá la pantalla
    # "No existe la informacion solicitada"
    # Se cuenta la cantidad de veces que se repite 'No existe' en el texto
    error_text = find_tag(
                report_tree.body.center.table.tr.td.table.tr.contents[3].table,
                                                                'No existe', 1)

    # Si hay mas de 0 'No' entonces se devuelve Falso
    if error_text:
        return False

    return html

def eliminar_comas(tag):
    """Elimina las comas del tag recibido, en caso no exista el atributo
    replace, devuelve False"""

    if hasattr(tag, 'replace'):
        return float(tag.replace(',', ''))
    else:
        return False

def hallar_valor(html, texto, tipo_ef, trim=''):
    """Encuentra el texto del tag buscado en el html"""

    th = html.find_all('th', text=texto)
    if th:
        # Los totales los EEFF los presentan utilizando un color gris oscuro
        # y el tag th en vez de td
        if tipo_ef == BALANCE:
            if hasattr(th[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                        next_sibling, 'text'):
                return th[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                         next_sibling.text
            else:
                return False
        elif tipo_ef == GANANCIA_PERDIDA :
            if trim == CONSTANT_ANHO:
                return th[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.text
            else:
                return th[0].next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.next_sibling.text
        elif tipo_ef == CAMBIO_PATRIMONIO:
            return th[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                         next_sibling.next_sibling.next_sibling.next_sibling. \
                         next_sibling.next_sibling.next_sibling.next_sibling. \
                         next_sibling.next_sibling.text
        elif tipo_ef == FLUJO_EFECTIVO:
            return th[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                         next_sibling.text
    else:
        # Los valores que no son resultado de sumar otros se ven en gris claro
        # y utilizan td como tag html.
        td = html.find_all('td', text=texto)
        if td:
            if tipo_ef == BALANCE:
                return td[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                           next_sibling.next_sibling.next_sibling.next_sibling.text
            elif tipo_ef == GANANCIA_PERDIDA:
                if trim == CONSTANT_ANHO:
                    return td[0].next_sibling.next_sibling.next_sibling. \
                                 next_sibling.next_sibling.next_sibling. \
                                 next_sibling.next_sibling.text
                else:
                    return td[0].next_sibling.next_sibling.next_sibling. \
                                 next_sibling.next_sibling.next_sibling. \
                                 next_sibling.next_sibling.text
            elif tipo_ef == CAMBIO_PATRIMONIO:
                return td[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.text
            elif tipo_ef == FLUJO_EFECTIVO:
                print td
                print td[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.next_sibling.next_sibling
                return td[0].next_sibling.next_sibling.next_sibling.next_sibling. \
                             next_sibling.next_sibling.next_sibling.next_sibling.text


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
                # Si el campo de la tabla tiene el atributo text, se devuelve
                # su valor
                if (tag_position < len(tag.contents) and
                    hasattr(tag.contents[tag_position], 'text')):
                    return tag.contents[tag_position].text


def none_entero(valor):

    if valor:
        return int(valor.replace(',',''))
    else:
        return valor
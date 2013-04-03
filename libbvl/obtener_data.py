#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Funciones para obtener data de los reportes financieros de la bolsa"""

from bs4 import BeautifulSoup

from utilitarios import report_html, find_tag, eliminar_comas

def obtener_data_bolsa(rpj, trimestre, anho):
    """Invoca a las funciones que obtienen data de cada reporte financieros"""

    data = {}

    data['periodo'] = anho + '-' + trimestre

    # Data del Balance General
    url_balance_general = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano={0}"
    "&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=BAL&Tipo1=T&Tipo2=I"
    "&Dsc_Correlativo=0000&Secuencia=0").format(anho, trimestre, rpj)

    # Agrega al diccionario la data de balance general 
    # En caso de que no existe, devuelve false
    data.update(balance_general_2010(url_balance_general))

    # Data del Estado de Ganancias y Pérdidas
    url_ganancias_perdidas = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=GYP&Tipo1=T&Tipo2=I&"
    "Dsc_Correlativo=0000&Secuencia=0").format(anho, trimestre, rpj)

    # Agrega el diccionario resultado de ganancias y perdidas a data
    # En caso de que no existe, devuelve false
    data.update(ganancias_perdidas_2010(url_ganancias_perdidas))

    # Data de Estado Flujos de Efectivo
    url_flujos_efectivo = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=EFE&Tipo1=T&Tipo2=I"
    "&Dsc_Correlativo=0000&Secuencia=0").format(anho, trimestre, rpj)

    # Agrega el diccionario resultado de flujos de efectivo a data.
    # Debido a que del año 2006 para abajo no hay datos sobre el flujo de
    # efectivo, se considera cero el valor en ese caso
    if int(anho) > 2006:
        data.update(flujo_efectivo_2010(url_flujos_efectivo))
    else:
        data.update({'flujo_efectivo': 0})

    # Data de Estado Flujos de Efectivo
    url_cambios_patrimonio = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=PAT&Tipo1=T&Tipo2=I&"
    "Dsc_Correlativo=0000&Secuencia=0").format(anho, trimestre, rpj)

    # Agrega el diccionario resultado de flujos de efectivo a data
    # En caso de que no existe, devuelve false
    data.update(estado_cambios_patrimonio_2010(url_cambios_patrimonio))

    return data


def balance_general_2010(url_balance_general):
    """Funcion que devuelve datos del Estado de flujos de efectivo formato
    2010"""

    data = {}

    html = report_html(url_balance_general)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html)

        # Obtenemos la tabla donde está ubicado el reporte
        reporte = \
        report_tree.body.contents[1].tr.contents[1].contents[1].contents[1]. \
                       contents[3].contents[1].contents[3].contents[1].table

        # Activos
        data['activos'] = eliminar_comas(find_tag(reporte, u'1D020T', 6))

        # Cuentas por cobrar
        data['cuentas_cobrar'] = eliminar_comas(find_tag(reporte,
                                                    u'1D0103', 9))

        # Activo circulante
        data['act_circulante'] = eliminar_comas(find_tag(reporte,
                                                    u'1D01ST', 6))

        # Inversiones de capital
        data['inv_capital'] = eliminar_comas(find_tag(reporte, u'1D02ST', 6))

        # En caso no exista alguno de los datos relacionados a activos se
        # calcula en base a los otros dos
        if (not data['activos'] and data['inv_capital']
            and data['act_circulante']):
            data['activos'] = data['inv_capital'] + data['act_circulante']

        elif (not data['inv_capital'] and data['activos']
            and data['act_circulante']):
            data['inv_capital'] = data['activos'] - data['act_circulante']

        elif (not data['act_circulante'] and data['activos']
            and data['inv_capital']):
            data['act_circulante'] = data['activos'] - data['inv_capital']

        # Deuda total
        data['deuda_total'] = float(find_tag(reporte,
                                         u'1D040T', 6).replace(',',''))

        # Deuda corto plazo
        data['deuda_corto_plazo'] = float(find_tag(reporte,
                                               u'1D03ST', 6).replace(',', ''))

        # Deuda largo plazo
        # En el año 2002 un reporte no tiene la data de deuda de largo plazo
        # por lo que se calcula utilizando la deuda total y la deuda de corto
        # plazo
        data['deuda_largo_plazo'] = \
                               data['deuda_total'] - data['deuda_corto_plazo']

        data['valor_libros'] = float(find_tag(reporte,
                                          u'1D07ST', 6).replace(',', ''))

        return data
    else:
        return False


def ganancias_perdidas_2010(url_ganancias_perdidas):
    """Funcion que devuelve datos del Estado de Ganancias y perdidas formato
    2010"""

    data = {}

    html = report_html(url_ganancias_perdidas)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html)

        # Obtenemos la tabla donde está ubicado el reporte
        reporte = \
        report_tree.body.center.table.contents[1].table.tr.contents[3]. \
                                             table.contents[3].td.table

        # Ingreso de actividades ordinarias
        data['ing_act_ord'] = float(find_tag(reporte,
                                         u'2D01ST', 7).replace(',', ''))

        # Ventas  
        data['ventas'] = float(find_tag(reporte,
                                    u'2D0101', 9).replace(',', ''))

        # Costo de la operacion
        data['costo_operacion'] = round(data['ventas']-data['ing_act_ord'], 3)

        # Utilidades
        data['utilidades'] = float(find_tag(reporte,
                                        u'2D07ST', 7).replace(',', ''))

        return data
    else:
        return False


def estado_cambios_patrimonio_2010(url_cambios_patrimonio):
    """Funcion que devuelve los valores del reporte de cambio de patrimonio
    formato 2010"""

    data = {}

    html = report_html(url_cambios_patrimonio)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html)

        # Obtenemos la tabla donde está ubicado el reporte
        reporte = \
        report_tree.body.center.table.tr.td.table.tr.contents[3].table. \
                                                   contents[3].td.table

        # Dividendos
        # Debido a que el texto 'Dividendos declarados y Participaciones
        # acordados durante el período/' se repite dos veces en el reporte 
        # se utiliza el codigo de la fila y obtenemos el total
        data['dividendos'] = float(find_tag(reporte,
                                       u'4D0204', 23).replace(',', ''))*-1

        # Emision de acciones con el nombre 'Nuevos Aportes de accionistas/'
        # Se usa el código de la fila para identificar la segunda fila que
        # corresponde a la fecha del reporte, no al año anterior
        data['emision_acciones'] = float(find_tag(reporte,
                                             u'4D0205', 23).replace(',', ''))

        # Si hay emision de acciones la variable es 1, caso contrario es 0
        if data['emision_acciones'] != 0:
            data['emision_acciones'] = 1

        return data
    else:
        return False

def flujo_efectivo_2010(url_flujos_efectivo):
    """Funcion que devuelve datos del Estado de flujos de efectivo formato 2010
    """

    data = {}

    html = report_html(url_flujos_efectivo)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:
        # Se obtiene el html del reporte
        report_tree = BeautifulSoup(html)

        # Se obtiene el html de la tabla donde esta el reporte
        reporte = \
        report_tree.body.center.table.contents[1].td.table.tr.contents[3] \
                                                       .contents[1].table

        # Se busca la fila requerida entre todos los descendientes de la tabla
        # Una vez que se encuentra la línea se obtiene el valor buscado
        data['flujo_efectivo'] = float(find_tag(reporte,
                                            u'3D08ST', 6).replace(',', ''))

        return data
    else:
        return False

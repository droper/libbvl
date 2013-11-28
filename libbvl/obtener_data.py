# -*- coding: utf-8 -*-

"""Funciones para obtener data de los reportes financieros de la bolsa"""

from bs4 import BeautifulSoup

from config import URL_BALANCE_GENERAL, URL_GANANCIAS_PERDIDAS, \
                   URL_FLUJOS_EFECTIVO, URL_CAMBIOS_PATRIMONIO, \
                   BALANCE, GANANCIA_PERDIDA, CAMBIO_PATRIMONIO, \
                   FLUJO_EFECTIVO, DICT_EMPRESAS

from utilitarios import report_html, find_tag, hallar_valor

def obtener_data_bolsa(rpj, trimestre, anho):
    """Invoca a las funciones que obtienen data de cada reporte financieros"""

    data = {}
    print trimestre, anho
    data['periodo'] = anho + '-' + trimestre

    # Data del Balance General
    url_balance_general = (URL_BALANCE_GENERAL).format(anho, trimestre, rpj)

    # Agrega al diccionario la data de balance general 
    # En caso de que no existe, devuelve false
    data.update(balance_general(url_balance_general))

    # Data del Estado de Ganancias y Pérdidas
    url_ganancias_perdidas = (URL_GANANCIAS_PERDIDAS).format(anho,
                                                    trimestre, rpj)

    # Agrega el diccionario resultado de ganancias y perdidas a data
    # En caso de que no existe, devuelve false
    data.update(ganancias_perdidas(url_ganancias_perdidas))

    # Data de Estado Flujos de Efectivo
    url_flujos_efectivo = (URL_FLUJOS_EFECTIVO).format(anho, trimestre, rpj)

    # Agrega el diccionario resultado de flujos de efectivo a data.
    # Debido a que del año 2006 para abajo no hay datos sobre el flujo de
    # efectivo, se considera cero el valor en ese caso
    if int(anho) > 2006:
        data.update(flujo_efectivo(url_flujos_efectivo))
    else:
        data.update({'flujo_efectivo': 0})

    # Data de Cambios en el Patrimonio
    url_cambios_patrimonio = (URL_CAMBIOS_PATRIMONIO).format(anho,
                                                         trimestre, rpj)

    # Agrega el diccionario resultado de flujos de efectivo a data
    # En caso de que no existe, devuelve false
    data.update(estado_cambios_patrimonio(url_cambios_patrimonio))

    return data


def balance_general(url_balance_general):
    """Funcion que devuelve datos del Estado de flujos de efectivo formato
    2010"""

    data = {}

    html = report_html(url_balance_general)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html, "html5lib")

        # Obtenemos la tabla donde está ubicado el reporte

        # Activos
        data['activos'] = hallar_valor(report_tree,
                                             u'1D020T', BALANCE)
        if data['activos']:
            data['activos'] = float(data['activos'].replace(',',''))

        # Cuentas por cobrar
        data['cuentas_cobrar'] = float(hallar_valor(report_tree,
                                       u'1D0103', BALANCE).replace(',',''))

        # Activo circulante
        data['act_circulante'] = float(hallar_valor(report_tree,
                                       u'1D01ST', BALANCE).replace(',',''))

        # Inversiones de capital
        data['inv_capital'] = hallar_valor(report_tree,u'1D02ST', BALANCE)

        if data['inv_capital']:
            data['inv_capital'] = float(data['inv_capital'].replace(',',''))
        else:
            data['inv_capital'] = 0

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
        data['deuda_total'] = float(hallar_valor(report_tree,
                                    u'1D040T', BALANCE).replace(',',''))

        # Deuda corto plazo
        data['deuda_corto_plazo'] = float(hallar_valor(report_tree,
                                    u'1D03ST', BALANCE).replace(',', ''))

        # Deuda largo plazo
        # En el año 2002 un reporte no tiene la data de deuda de largo plazo
        # por lo que se calcula utilizando la deuda total y la deuda de corto
        # plazo
        data['deuda_largo_plazo'] = \
                               data['deuda_total'] - data['deuda_corto_plazo']

        data['valor_libros'] = float(hallar_valor(report_tree,
                                          u'1D07ST', BALANCE).replace(',', ''))

    else:
        data['activos'] = 0
        data['cuentas_cobrar'] = 0
        data['act_circulante'] = 0
        data['inv_capital'] = 0
        data['deuda_total'] = 0
        data['deuda_corto_plazo'] = 0
        data['deuda_largo_plazo'] = 0
        data['valor_libros'] = 0

    return data

def ganancias_perdidas(url_ganancias_perdidas):
    """Funcion que devuelve datos del Estado de Ganancias y perdidas formato
    2010"""

    data = {}

    html = report_html(url_ganancias_perdidas)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html, "html.parser")

        # Ingreso de actividades ordinarias
        data['ing_act_ord'] = float(hallar_valor(report_tree,
                               u'2D01ST', GANANCIA_PERDIDA).replace(',', ''))

        # Si no hay ventas como partida aparte, entonces los ingresos de
        # actividades ordinarias son iguales a las ventas
        ventas =  hallar_valor(report_tree, u'2D0101', GANANCIA_PERDIDA)
        if ventas:
            data['ventas'] = float(ventas.replace(',', ''))
        else:
            data['ventas'] = data['ing_act_ord']

        # Costo de la operacion
        #data['costo_operacion'] = round(data['ventas']-data['ing_act_ord'], 3)

        data['costo_operacion'] = hallar_valor(report_tree, '2D0203',
                                                     GANANCIA_PERDIDA)
        if data['costo_operacion']:
            data['costo_operacion'] = float(hallar_valor(report_tree,
                             '2D0203', GANANCIA_PERDIDA).replace(',', ''))

        # Costo de las ventas
        data['costo_ventas'] = hallar_valor(report_tree, '2D0201',
                                                     GANANCIA_PERDIDA)
        if data['costo_ventas']:
            data['costo_ventas'] = float(hallar_valor(report_tree,
                             '2D0201', GANANCIA_PERDIDA).replace(',', ''))

        # Utilidades
        data['utilidades'] = float(hallar_valor(report_tree,
                             '2D07ST', GANANCIA_PERDIDA).replace(',', ''))

    else:
        data['ing_act_ord'] = 0
        data['ventas'] = 0
        data['costo_operacion'] = 0
        data['utilidades'] = 0
        data['costo_ventas'] = 0

    return data

def estado_cambios_patrimonio(url_cambios_patrimonio):
    """Funcion que devuelve los valores del reporte de cambio de patrimonio
    formato 2010"""

    data = {}

    html = report_html(url_cambios_patrimonio)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html, "html.parser")

        # Dividendos
        # Debido a que el texto 'Dividendos declarados y Participaciones
        # acordados durante el período/' se repite dos veces en el reporte 
        # se utiliza el codigo de la fila y obtenemos el total
        data['dividendos'] = float(hallar_valor(report_tree,
                             u'4D0204', CAMBIO_PATRIMONIO).replace(',', ''))*-1

        # Emision de acciones con el nombre 'Nuevos Aportes de accionistas/'
        # Se usa el código de la fila para identificar la segunda fila que
        # corresponde a la fecha del reporte, no al año anterior
        data['emision_acciones'] = float(hallar_valor(report_tree,
                                u'4D0205', CAMBIO_PATRIMONIO).replace(',', ''))

        # Si hay emision de acciones la variable es 1, caso contrario es 0
        if data['emision_acciones'] != 0:
            data['emision_acciones'] = 1

    else:

        data['dividendos'] = 0
        data['emision_acciones'] = 0

    return data

def flujo_efectivo(url_flujos_efectivo):
    """Funcion que devuelve datos del Estado de flujos de efectivo formato 2010
    """

    data = {}

    html = report_html(url_flujos_efectivo)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:
        # Se obtiene el html del reporte
        report_tree = BeautifulSoup(html, "html5lib")

        # Se busca la fila requerida entre todos los descendientes de la tabla
        # Una vez que se encuentra la línea se obtiene el valor buscado 
        if hallar_valor(report_tree, u'3D01ST', FLUJO_EFECTIVO):
            data['flujo_efectivo'] = float(hallar_valor(report_tree,
                                  u'3D01ST', FLUJO_EFECTIVO).replace(',', ''))
        else:
           data['flujo_efectivo'] = 0
    else:

        data['flujo_efectivo'] = 0

    return data

# -*- coding: utf-8 -*-

"""Funciones para obtener data de los reportes financieros de la bolsa"""

from bs4 import BeautifulSoup

from config import URL_BALANCE_GENERAL, URL_GANANCIAS_PERDIDAS, \
                   URL_FLUJOS_EFECTIVO, URL_CAMBIOS_PATRIMONIO, \
                   BALANCE, GANANCIA_PERDIDA, CAMBIO_PATRIMONIO, \
                   FLUJO_EFECTIVO, CONSTANT_ANHO, \
                   CONSTANT_TRIM, ASIENTOS_FLUJO_EFECTIVO, \
                   ASIENTOS_CAMBIO_PATRIMONIO, ASIENTOS_GANANCIAS_PERDIDAS, \
                   ASIENTOS_BALANCE_GENERAL

from utilitarios import report_html, hallar_valor, none_entero, leer_asientos


def obtener_data_bolsa(rpj, trimestre, anho):
    """Invoca a las funciones que obtienen data de cada reporte financieros"""

    data = {}
    print trimestre, anho
    data['Periodo'] = anho + '-' + trimestre

    if trimestre == CONSTANT_ANHO:
        trim = CONSTANT_ANHO
    else:
        trim = CONSTANT_TRIM

    # Data del Balance General
    url_balance_general = (URL_BALANCE_GENERAL).format(anho, trimestre, rpj, trim)

    # Agrega al diccionario la data de balance general 
    # En caso de que no existe, devuelve false
    data.update(balance_general(url_balance_general))

    # Data del Estado de Ganancias y Pérdidas
    url_ganancias_perdidas = (URL_GANANCIAS_PERDIDAS).format(anho,
                                                    trimestre, rpj, trim)

    # Agrega el diccionario resultado de ganancias y perdidas a data
    # En caso de que no existe, devuelve false
    data.update(ganancias_perdidas(url_ganancias_perdidas))

    # Data de Estado Flujos de Efectivo
    url_flujos_efectivo = (URL_FLUJOS_EFECTIVO).format(anho, trimestre, rpj, trim)

    # Agrega el diccionario resultado de flujos de efectivo a data.
    # Debido a que del año 2006 para abajo no hay datos sobre el flujo de
    # efectivo, se considera cero el valor en ese caso
    if int(anho) > 2006:
        data.update(flujo_efectivo(url_flujos_efectivo))
    else:
        #data.update({'flujo_efectivo': 0})
        data.update({'depreciacion': 0})

    # Data de Cambios en el Patrimonio
    url_cambios_patrimonio = (URL_CAMBIOS_PATRIMONIO).format(anho,
                                                         trimestre, rpj, trim)

    # Agrega el diccionario resultado de cambios de patrimonio a data
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

        # Lee los asientos del balance general de la web de la bvl
        # y actualiza el diccionario data con los resultados
        data.update(leer_asientos(ASIENTOS_BALANCE_GENERAL, report_tree, BALANCE))

        # Obtenemos la tabla donde está ubicado el reporte

        data['cuentas_cobrar'] = 0

        if '1D0103' in ASIENTOS_BALANCE_GENERAL:
            data['cuentas_cobrar'] += data[ASIENTOS_BALANCE_GENERAL['1D0103']]
            del data[ASIENTOS_BALANCE_GENERAL['1D0103']]
        if '1D0104' in ASIENTOS_BALANCE_GENERAL:
            data['cuentas_cobrar'] += data[ASIENTOS_BALANCE_GENERAL['1D0104']]
            del data[ASIENTOS_BALANCE_GENERAL['1D0104']]
        if '1D0105' in ASIENTOS_BALANCE_GENERAL:
            data['cuentas_cobrar'] += data[ASIENTOS_BALANCE_GENERAL['1D0105']]
            del data[ASIENTOS_BALANCE_GENERAL['1D0105']]


        # Si no hay datos sobre inversiones de capital entonces el valor es cero
        if not data['inv_capital']:
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

        # Deuda largo plazo
        # En el año 2002 un reporte no tiene la data de deuda de largo plazo
        # por lo que se calcula utilizando la deuda total y la deuda de corto
        # plazo
        if data['deuda_total'] and data['deuda_corto_plazo']:
            data['deuda_largo_plazo'] = \
                               data['deuda_total'] - data['deuda_corto_plazo']

        #data['valor_libros'] = none_entero(hallar_valor(report_tree,
        #                                                u'1D07ST', BALANCE))

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

    # Si es el reporte de un año se le da el valor de A a trim
    # Para que la función hallar_valor distinga entre los reportes
    # trimestrales y los anuales
    trim = 'T'
    if "Trimestre=A" in url_ganancias_perdidas:
        trim = CONSTANT_ANHO

    html = report_html(url_ganancias_perdidas)

    # Si el url existe y devuelve un html valido, se obtienen los valores
    # caso contrario no se hace nada
    if html:

        # Parse the report html
        report_tree = BeautifulSoup(html, "html.parser")

        data.update(leer_asientos(ASIENTOS_GANANCIAS_PERDIDAS, report_tree,
                                   GANANCIA_PERDIDA))

        # Si no hay ventas como partida aparte, entonces los ingresos de
        # actividades ordinarias son iguales a las ventas
        if not data['ventas']:
            data['ventas'] = data['Ingreso total']

        # Si no se encuentra data para costo de operación, entonces se prueba con otro asiento.
        if not data['costo_operacion']:
            data['costo_operacion'] = none_entero(hallar_valor(report_tree, '2D0201',
                                                               GANANCIA_PERDIDA, trim))

    else:
        data['Ingreso total'] = 0
        data['ventas'] = 0
        data['costo_operacion'] = 0
        data['gastos_financieros'] = 0
        data['ganancia_operacion'] = 0
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

        #for llave, valor in ASIENTOS_CAMBIO_PATRIMONIO.items():
        #    data[valor] = none_entero(hallar_valor(report_tree, llave,
        #                                           CAMBIO_PATRIMONIO))

        data.update(leer_asientos(ASIENTOS_CAMBIO_PATRIMONIO, report_tree,
                                   CAMBIO_PATRIMONIO))

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
        # Si el flujo de efectivo no está en el asiento 3D01ST se busca en el
        # asiento 3D08ST
        #data['flujo_efectivo'] = hallar_valor(report_tree, u'3D01ST',
        #                                               FLUJO_EFECTIVO)

        data.update(leer_asientos(ASIENTOS_FLUJO_EFECTIVO, report_tree,
                                   FLUJO_EFECTIVO))


        """
        if data['flujo_efectivo']:
            data['flujo_efectivo'] = \
                         int(data['flujo_efectivo'].replace(',', ''))
            data['Depreciacion'] = \
                         int(data['Depreciacion'].replace(',', ''))
        else:
            data['flujo_efectivo'] = int(hallar_valor(report_tree, u'3D08ST',
                                              FLUJO_EFECTIVO).replace(',', ''))
        """
    else:
        #data['flujo_efectivo'] = 0
        data['depreciacion']   = 0

    return data

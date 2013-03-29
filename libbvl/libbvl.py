#!/usr/bin/python
# -*- coding: utf-8 -*-

from funciones_formato_2011 import report_data_2011
from funciones_formato_2010 import report_data_2010
from funciones_formato_2006 import report_data_2006
from funciones_formato_2002 import report_data_2002

def obtener_data_bolsa(rpj, trimestre, anho):

    if int(anho) >= 2011:
       data = report_data_2011(rpj, trimestre, anho)
    elif int(anho) >= 2007:
       data = report_data_2010(rpj, trimestre, anho)
    elif int(anho) >= 2003:
       data = report_data_2006(rpj, trimestre, anho)
    elif int(anho) >= 2000:
       data = report_data_2002(rpj, trimestre, anho)

    return data


def generar_variables(data):

    #Se identifica si la data es valida
    if(data):

            variables = {}

            variables['periodo'] = data['periodo']

            variables['roa'] = round(data['ing_act_ord']/data['activos'],3)
            variables['roe'] = round(data['ing_act_ord']/data['valor_libros'],3)
            variables['roa_fc'] = round(data['flujo_efectivo']/data['activos'],3)

            #Si no hay utilidades,el ratio es cero
            if data['utilidades']:
                variables['ratio_dividendos_utilidades'] = \
                round(data['dividendos']/data['utilidades'],3)
            else:
                variables['ratio_dividendos_utilidades'] = 0

            #Si los ingresos son mayores que el flujo de efectivo hay ajustes
            if data['ing_act_ord'] > data['flujo_efectivo']:
               variables['ajustes']  = 1
            else:
               variables['ajustes']  = 0

            variables['liquidez'] = round(data['act_circulante']/data['deuda_corto_plazo'],3)
            variables['ratio_deuda_largo_plazo'] = round(data['deuda_largo_plazo']/data['activos'],3)
            variables['emision_acciones'] = int(data['emision_acciones'])
            variables['utilidades'] = round(data['utilidades'],3)

            return variables
    else:
            return False





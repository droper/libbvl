#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from utilitarios import report_html, find_tag

def report_data_2010(rpj, trimestre, anho):
    """Utiliza data de los periodos 2010, 2009, 2008 y 2007"""

    data = {}

    data['periodo'] = anho+'-'+trimestre

    #Data del Balance General
    url_balance_general = \
    "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=BAL&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    #Agrega el diccionario la data de balance general 
    #En caso de que no existe, devuelve false
    data.update(balance_general_2010(url_balance_general))

    #Data del Estado de Ganancias y Pérdidas
    url_ganancias_perdidas = \
    "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=GYP&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    #Agrega el diccionario resultado de ganancias y perdidas a data
    #En caso de que no existe, devuelve false
    data.update(ganancias_perdidas_2010(url_ganancias_perdidas))

    #Data de Estado Flujos de Efectivo
    url_flujos_efectivo = \
    "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=EFE&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    #Agrega el diccionario resultado de flujos de efectivo a data
    #En caso de que no existe, devuelve false
    data.update(flujo_efectivo_2010(url_flujos_efectivo))

    #Data de Estado Flujos de Efectivo
    url_cambios_patrimonio = \
    "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=PAT&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    #Agrega el diccionario resultado de flujos de efectivo a data
    #En caso de que no existe, devuelve false
    data.update(estado_cambios_patrimonio_2010(url_cambios_patrimonio))

    return data


#Funcion que devuelve datos del Estado de Ganancias y perdidas formato 2010
def ganancias_perdidas_2010(url_ganancias_perdidas):

    data = {}

    html = report_html(url_ganancias_perdidas)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:

            #Parse the report html
            report_tree = BeautifulSoup(html)

            #Obtenemos la tabla donde está ubicado el reporte
            reporte =\
            report_tree.body.center.table.contents[1].table.tr.contents[3].table.contents[3].td.table

            #Ingreso de actividades ordinarias
            data['ing_act_ord'] = \
            float(find_tag(reporte, u'Total de Ingresos Brutos', 7).replace(',',''))

            #Ventas  
            data['ventas'] = \
            float(find_tag(reporte, u'Ventas Netas (ingresos operacionales)', 9).replace(',',''))

            #Costo de la operacion
            data['costo_operacion'] = round(data['ventas'] - data['ing_act_ord'],3)

            #Utilidades
            data['utilidades'] = \
            float(find_tag(reporte, u'Utilidad (Perdida)  Neta del Ejercicio', 7).replace(',',''))

            return data
    else:
            return False

#Funcion que devuelve datos del Estado de flujos de efectivo formato 2010
def flujo_efectivo_2010(url_flujos_efectivo):

    data = {}

    html = report_html(url_flujos_efectivo)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:
            #Parse the report html
            report_tree = BeautifulSoup(html)

            #Se obtiene el html de la tabla donde esta el report 
            reporte =report_tree.body.center.table.contents[1].td.table.tr.contents[3].contents[1].table

            #Se busca la fila requerida entre todos los descendientes de la tabla
            #Una vez que se encuentra la línea se obtiene el valor buscado
            data['flujo_efectivo'] = \
            float(find_tag(reporte, u'Aumento (Disminución) del Efectivo y ' \
            + u'Equivalente de Efectivo Provenientes de Actividades de Operación',6).replace(',',''))

            return data
    else:
            return False

#Funcion que devuelve datos del Estado de flujos de efectivo formato 2010
def balance_general_2010(url_balance_general):

    data = {}

    html = report_html(url_balance_general)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:

            #Parse the report html
            report_tree = BeautifulSoup(html)

            #Obtenemos la tabla donde está ubicado el reporte
            reporte =\
            report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].table

            #Activos
            data['activos'] = float(find_tag(reporte, u'TOTAL ACTIVO/', 6).replace(',',''))

            #Cuentas por cobrar
            data['cuentas_cobrar'] = \
            float(find_tag(reporte, u'Cuentas por Cobrar Comerciales (neto)/', 9).replace(',',''))

            #Inversiones de capital
            data['inv_capital'] = \
            float(find_tag(reporte, u'Total Activo No Corriente/', 6).replace(',',''))

            #Activo circulante
            data['act_circulante'] = \
            float(find_tag(reporte, u'Total Activo Corriente/', 6).replace(',',''))

            #Deuda corto plazo
            data['deuda_corto_plazo'] = \
            float(find_tag(reporte, u'Total Pasivo Corriente/', 6).replace(',',''))

            #Deuda largo plazo
            data['deuda_largo_plazo'] = \
            float(find_tag(reporte, u'Total Pasivo No Corriente/', 6).replace(',',''))

            data['valor_libros'] = \
            float(find_tag(reporte, u'Total Patrimonio Neto/', 6).replace(',',''))

            return data
    else:
            return False

#Funcion que devuelve los valores del reporte de cambio de patrimonio formato
#2010
def estado_cambios_patrimonio_2010(url_cambios_patrimonio):

    data = {}

    html = report_html(url_cambios_patrimonio)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:

            #Parse the report html
            report_tree = BeautifulSoup(html)

            #Obtenemos la tabla donde está ubicado el reporte
            reporte =\
            report_tree.body.center.table.tr.td.table.tr.contents[3].table.contents[3].td.table
            #report_tree.body.center.table.contents[1].td.table.tr.contents[3].table.contents[5].td.table

            #Dividendos
            #Debido a que el texto 'Dividendos declarados y Participaciones
            #acordados durante el período/' se repite dos veces en el reporte 
            #se utiliza el codigo de la fila y obtenemos el total
            data['dividendos'] = float(find_tag(reporte,u'4D0204', 23).replace(',',''))*-1

            #Emision de acciones con el nombre 'Nuevos Aportes de accionistas/'
            #Se usa el código de la fila para identificar la segunda fila que
            #corresponde a la fecha del reporte, no al año anterior
            data['emision_acciones'] = float(find_tag(reporte,u'4D0205', 23).replace(',',''))

            #Si hay emision de acciones la variable es 1, caso contrario es 0
            if data['emision_acciones'] <> 0:
                data['emision_acciones'] = 1

    else:
            return False

    return data

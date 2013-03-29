#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from utilitarios import report_html, find_tag

def report_data_2011(rpj, trimestre, anho):

    data = {}

    data['periodo'] = anho+'-'+trimestre

    ############Data from Estado de Resultados############

    #Report url
    url_resultados = "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=GYP&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    html = report_html(url_resultados)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:

            #Parse the report html
            report_tree = BeautifulSoup(html)

            #Ingreso de actividades ordinarias
            data['ing_act_ord'] = float(report_tree.body.center.table.contents[1].table.tr.contents[3].table.contents[3].td.table.contents[29].contents[7].text.replace(',',''))

            #Ventas
            data['ventas'] = float(report_tree.body.center.table.contents[1].table.tr.contents[3].table.contents[3].td.table.contents[13].contents[7].text.replace(',',''))

            #Costo de la operacion
            data['costo_operacion'] = round(data['ventas'] - data['ing_act_ord'],3)

            #Utilidades
            data['utilidades'] = float(report_tree.body.center.table.contents[1].table.tr.contents[3].table.contents[3].td.table.contents[49].contents[7].text.replace(',',''))

    else:
            return False

    ###########Data from Estado Situacion financiera#########

    url_situacion_financiera = "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=BAL&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    html = report_html(url_situacion_financiera)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:

            #Parse the report html
            report_tree = BeautifulSoup(html)

            #Activos
            data['activos'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[69].contents[8].text.replace(',',''))

            #Cuentas por cobrar
            data['cuentas_cobrar'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[15].contents[9].text.replace(',',''))

            #Inversiones de capital
            data['inv_capital'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[57].contents[11].text.replace(',',''))

            #Activo circulante
            data['act_circulante'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[11].contents[9].text.replace(',',''))

            #Deuda corto plazo
            data['deuda_corto_plazo'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[95].contents[6].text.replace(',',''))

            #Deuda largo plazo
            data['deuda_largo_plazo'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[117].contents[6].text.replace(',',''))

            data['valor_libros'] = float(report_tree.body.contents[1].tr.contents[1].contents[1].contents[1].contents[3].contents[1].contents[3].contents[1].contents[1].contents[137].contents[6].text.replace(',',''))

    else:
            return False

    ###########Data de Estado Flujos de Efectivo#############

    url_flujos_efectivo = "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=EFE&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

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
            for tag in reporte.descendants:
                try:
                   if tag.text.count('Flujos de Efectivo y Equivalente al Efectivo Procedente de (Utilizados en) Actividades de Operac') > 0:
                      data['flujo_efectivo'] = float(tag.next_sibling.next_sibling.next_sibling.text.replace(',',''))
                except:
                   pass

    else:
            return False

    ###########Data de Estado cambios patrimonio#############

    url_cambios_patrimonio = "http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="+anho+"&Trimestre="+trimestre+"&Rpj="+rpj+"&RazoSoci=&TipoEEFF=PAT&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0"

    html = report_html(url_cambios_patrimonio)

    #Si el url existe y devuelve un html valido, se obtienen los valores
    #caso contrario no se hace nada
    if html:

            #Parse the report html
            report_tree = BeautifulSoup(html)

            reporte =\
            report_tree.body.center.table.contents[1].td.table.tr.contents[3].table.contents[3].td.table

            #4D0204 es el código en el reporte de Dividendos
            data['dividendos'] = \
            float(find_tag(reporte, u'4D0204', 33).replace(',',''))*-1

            #4D0205 es el código en el reporte de la Emision de acciones
            data['emision_acciones'] = \
            float(find_tag(reporte, u'4D0205', 33).replace(',',''))

            #Si hay emision de acciones la variable es 1, caso contrario es 0
            if data['emision_acciones'] <> 0:
                data['emision_acciones'] = 1

    else:
            return False

    return data


#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Las funciones para generar el archivo csv"""

import csv

def generar_csv(lista_variables, empresa, nombre_archivo='', directorio='.'):
    """Funcion que genera el csv con la lista de valores de cada año"""

    # Si el parámetro nombre_archivo tiene el valor por defecto, se asigna el
    # nombre por defecto al archivo.
    if len(nombre_archivo) == 0:
        nombre_archivo = 'variables_'+empresa+'.csv'

    # El nombre de los campos en el csv
    nombre_campos = ['periodo', 'roa', 'roa_fc', 'emision_acciones', 'roe', \
                     'ratio_dividendos_utilidades', 'utilidades', \
                      'ratio_deuda_largo_plazo', 'ajustes', 'liquidez']

    # Se crea el archivo donde se van a guardar los valores y se escriben en
    # formato csv 
    with open(directorio + '/'+nombre_archivo, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(nombre_campos)

        # Se escriben los valores del diccionario de cada año en el csv
        for dict_variable in lista_variables:
            writer_dict = \
            csv.DictWriter(csvfile, fieldnames=nombre_campos, dialect='excel')
            writer_dict.writerow(dict_variable)



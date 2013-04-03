#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Las funciones para generar el archivo csv"""

import csv

def generar_csv(lista_variables, empresa, nombre_archivo='', directorio='.'):
    """Funcion que genera el csv con la lista de valores de cada año"""

    # El nombre de los campos en el csv
    nombre_campos = lista_variables[0].keys()
    nombre_campos.insert(0, nombre_campos.pop(nombre_campos.index('periodo')))

    # Si el parámetro nombre_archivo tiene el valor por defecto, se asigna el
    # nombre por defecto al archivo. El nombre de archivo incluye el codigo de
    # la empresa y los periodos que abarca la lista de datos 
    if nombre_archivo == '':
        nombre_archivo = 'variables_' + empresa + '-' + \
                         lista_variables[0]['periodo'] + '-' +  \
        lista_variables[len(lista_variables)-1]['periodo'] + '.csv'

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



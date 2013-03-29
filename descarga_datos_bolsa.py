#!/usr/bin/python
# -*- coding: utf-8 -*-

from libbvl import obtener_data_bolsa, generar_variables, generar_csv, \
                   dict_empresas, rpj_empresas

#Report parameters
num_trimestres = 4
anho_fin = 2012
anho_inicio = 2012


num = 1

datos_anhos = []

#Obtiene las variables para todos los anhos
for anho in range (anho_inicio,anho_fin+1):
    print anho
    for trimestre in range(num_trimestres,0,-1):
        print trimestre
        variables = generar_variables(obtener_data_bolsa(rpj_empresas[num],str(trimestre),str(anho)))
        #Si no existe el url debido a que aún se ha llegado al trimestre solicitado
        #generar_variables devuelve False y no se hace nada
        if variables:
           datos_anhos.append(variables)


#Genera el csv con el nombre de la empresa
generar_csv(datos_anhos,dict_empresas[rpj_empresas[num]])

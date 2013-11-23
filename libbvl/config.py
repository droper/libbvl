#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Parámetros de la libreria"""

#URL_BALANCE_GENERAL = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano={0}"
#    "&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=BAL&Tipo1=T&Tipo2=I"
#    "&Dsc_Correlativo=0000&Secuencia=0")

URL_BALANCE_GENERAL = ("/home/pedro/univs/doctorado/tesis/"
                      "libbvl/pages/Estados Financieros.html")

URL_GANANCIAS_PERDIDAS = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=GYP&Tipo1=T&Tipo2=I&"
    "Dsc_Correlativo=0000&Secuencia=0")

URL_FLUJOS_EFECTIVO = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=EFE&Tipo1=T&Tipo2=I"
    "&Dsc_Correlativo=0000&Secuencia=0")

URL_CAMBIOS_PATRIMONIO = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=PAT&Tipo1=T&Tipo2=I&"
    "Dsc_Correlativo=0000&Secuencia=0")

DICT_EMPRESAS = {'002597':'Corona', 'CM0004':'Shougang',
                 'B20001':'Castrovirreyna', 'B20023':'Perubar',
                 'CM0006':'Cerro Verde'}

TRIMESTRE_INICIAL = 1
TRIMESTRE_FINAL = 4


#!/usr/bin/python
# -*- coding: utf-8 -*-

from libbvl import datos_empresa, ratios_empresa, ratios_empresa_csv, \
                   datos_empresa_csv, DICT_EMPRESAS


#for key in DICT_EMPRESAS.keys():
#    print DICT_EMPRESAS[key]
#    datos_empresa_csv(key,2000, 4, 2013, 3)

datos_empresa_csv('CM0001',2000, 1, 2013, 3)

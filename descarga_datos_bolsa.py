#!/usr/bin/python
# -*- coding: utf-8 -*-

from libbvl import datos_empresa, ratios_empresa, ratios_empresa_csv, \
                   datos_empresa_csv, DICT_EMPRESAS


#for key in DICT_EMPRESAS.keys():
#    print DICT_EMPRESAS[key]
#    datos_empresa_csv(key,2000, 4, 2014, 4)

datos_empresa('B20010', 2004, 1, 2012, 4)

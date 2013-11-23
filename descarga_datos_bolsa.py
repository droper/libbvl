#!/usr/bin/python
# -*- coding: utf-8 -*-

from libbvl import datos_empresa, ratios_empresa, ratios_empresa_csv, \
                   datos_empresa_csv, DICT_EMPRESAS


#ratios_anhos = ratios_empresa(RPJ_EMPRESAS[num_empresa],2004,2,2008,3)
datos_anhos = datos_empresa_csv(111,2013, 3,2013, 3)
#datos_anhos = datos_empresa_csv(RPJ_EMPRESAS[num_empresa],2010, 1,2010, 1)
#datos_anhos = datos_empresa_csv(RPJ_EMPRESAS[num_empresa],2003, 1,2003, 1)
#datos_anhos = datos_empresa_csv('CM0004', 2002, 1,2002, 1)
#print ratios_empresa('002597', 2000, 4, 2000,4)
#print ratios_empresa('002597', 2003, 4, 2003,4)
#print ratios_empresa('002597', 2008, 4, 2008,4)
#print ratios_empresa('002597', 2013, 1, 2012,3)


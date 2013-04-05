#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Batería de tests para libbvl"""

from libbvl import datos_empresa, ratios_empresa, DICT_EMPRESAS

def test_datos_empresa():

    datos_2000_orig = [{'deuda_corto_plazo': 26536.0, 'flujo_efectivo': 0,
    'act_circulante': 64572.0, 'activos': 164100.0, 'periodo': '2000-4',
    'inv_capital': 99528.0, 'emision_acciones': 0.0, 'utilidades': 1869.0,
    'ing_act_ord': 39036.0, 'dividendos': 18193.0, 'valor_libros': 134911.0,
    'deuda_total': 29189.0, 'cuentas_cobrar': 26263.0, 'deuda_largo_plazo':
    2653.0, 'costo_operacion': 0.0, 'ventas': 39036.0}]

    datos_2003_orig = [{'deuda_corto_plazo': 45553.0, 'flujo_efectivo': 0,
    'act_circulante': 68241.0, 'activos': 156392.0, 'periodo': '2003-4',
    'inv_capital': 88151.0, 'emision_acciones': 0.0, 'utilidades': 120.0,
    'ing_act_ord': 54787.0, 'dividendos': 7203.0, 'valor_libros': 110839.0,
    'deuda_total': 45553.0, 'cuentas_cobrar': 22497.0, 'deuda_largo_plazo':
    0.0, 'costo_operacion': -8420.0, 'ventas': 46367.0}]

    datos_2008_orig = [{'deuda_corto_plazo': 9029.0, 'flujo_efectivo': 27262.0,
    'act_circulante': 16681.0, 'activos': 53241.0, 'periodo': '2008-4',
    'inv_capital': 36560.0, 'emision_acciones': 0.0, 'utilidades': 1265.0,
    'ing_act_ord': 16175.0, 'dividendos': 21204.0, 'valor_libros': 22619.0,
    'deuda_total': 30622.0, 'cuentas_cobrar': 4023.0, 'deuda_largo_plazo':
    21593.0, 'costo_operacion': -1735.0, 'ventas': 14440.0}]

    datos_2012_orig = [{'deuda_corto_plazo': 37869.0, 'flujo_efectivo':
    56273.0, 'act_circulante': 96653.0, 'activos': 141826.0, 'periodo':
    '2012-4', 'inv_capital': 45173.0, 'emision_acciones': 0.0, 'utilidades':
    6989.0, 'ing_act_ord': 35989.0, 'dividendos': -0.0, 'valor_libros':
    89595.0, 'deuda_total': 52231.0, 'cuentas_cobrar': 15294.0,
    'deuda_largo_plazo': 14362.0, 'costo_operacion': 0.0, 'ventas': 35989.0}]

    assert datos_2000_orig == datos_empresa('002597', 2000, 4, 2000,4)
    assert datos_2003_orig == datos_empresa('002597', 2003, 4, 2003,4)
    assert datos_2008_orig == datos_empresa('002597', 2008, 4, 2008,4)
    assert datos_2012_orig == datos_empresa('002597', 2012, 4, 2012,4)


def test_ratios_empresa():
    pass

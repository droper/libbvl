#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Batería de tests para libbvl"""

from libbvl import datos_empresa, ratios_empresa, DICT_EMPRESAS

def test_datos_empresa():
    """Se hace el test de la función datos_empresa(), comparandose con cuatro
       resultados de la empresa minera Corona.
    """

    datos_2000_orig = {'ganancia_operacion': 3682, 'deuda_corto_plazo': 26536,
    'gasto_ventas_distribucion': -4107, 'Ingreso total': 39036,
    'act_circulante': 64572, 'activos': 164100, 'Periodo': '2000-4',
    'inv_capital': 99528, 'gastos_administracion': -3629, 'gastos_financieros': -124,
    'dividendos': 0, 'utilidades': 1869, 'costo_ventas': -27618,
    'valor_libros': 134911.0, 'deuda_total': 29189.0, 'cuentas_cobrar': 30575,
    'emision_acciones': 0.0, 'deuda_largo_plazo': 2653, 'depreciacion': 0,
    'costo_operacion': -27618, 'ventas': 39036}

    datos_2003_orig = {'ganancia_operacion': 11509, 'deuda_corto_plazo': 45553.0,
    'gasto_ventas_distribucion': -3177, 'Ingreso total': 54787.0,
    'act_circulante': 68241.0, 'activos': 156392.0, 'Periodo': '2003-4',
    'inv_capital': 88151.0, 'gastos_administracion': -3846, 'gastos_financieros': -91,
    'dividendos': 0, 'utilidades': 120.0, 'costo_ventas': -31854,
    'valor_libros': 110839.0,  'deuda_total': 45553.0, 'cuentas_cobrar': 26135,
    'emision_acciones': 0, 'deuda_largo_plazo': 0.0, 'depreciacion': 0,
    'costo_operacion': -36255, 'ventas': 46367.0}

    datos_2008_orig = {'ganancia_operacion': 3600, 'deuda_corto_plazo': 9029.0,
    'gasto_ventas_distribucion': -1517, 'Ingreso total': 16175.0,
    'act_circulante': 16681.0, 'activos': 53241.0, 'Periodo': '2008-4',
    'inv_capital': 36560.0, 'gastos_administracion': -1314, 'gastos_financieros': -1352,
    'dividendos': 21204.0, 'utilidades': 1265.0, 'costo_ventas': -7367,
    'valor_libros': 22619.0, 'deuda_total': 30622.0, 'cuentas_cobrar': 5013.0,
    'emision_acciones': 0.0, 'deuda_largo_plazo': 21593.0, 'depreciacion': 4457,
    'costo_operacion': -8418.0, 'ventas': 14440.0}

    datos_2012_orig = {'ganancia_operacion': 11897, 'deuda_corto_plazo': 37869.0,
    'gasto_ventas_distribucion': -1176 	, 'Ingreso total': 35989.0,
    'act_circulante': 96653.0, 'activos': 141826.0, 'Periodo': '2012-4',
    'inv_capital': 45173.0, 'gastos_administracion': -3909, 'gastos_financieros': -257,
    'dividendos': 30892, 'utilidades': 6989.0, 'costo_ventas': -16817,
    'valor_libros': 89595.0, 'deuda_total': 52231.0, 'cuentas_cobrar': 15775.0,
    'emision_acciones': 0.0, 'deuda_largo_plazo': 14362.0, 'depreciacion': 0,
    'costo_operacion': -16817, 'ventas': 35989.0}

    assert datos_2000_orig == datos_empresa('002597', 2000, 4, 2000,4)[0]
    assert datos_2003_orig == datos_empresa('002597', 2003, 4, 2003,4)[0]
    assert datos_2008_orig == datos_empresa('002597', 2008, 4, 2008,4)[0]
    assert datos_2012_orig == datos_empresa('002597', 2012, 4, 2012,4)[0]

    print "Paso test de datos empresa"


def test_ratios_empresa():
    """Se hace el test de la función ratios_empresa(), comparandose con cuatro
       resultados para comprobar si la función está bien.
    """

    ratios_2000_orig = {'periodo': '2000-4', 'roa_fc': 0.0,
    'emision_acciones': 0, 'roe': 0.289, 'ratio_dividendos_utilidades': 9.734,
    'utilidades': 1869.0, 'ratio_deuda_largo_plazo': 0.016, 'roa': 0.238,
    'ajustes': 1, 'liquidez': 2.433}

    ratios_2003_orig = {'periodo': '2003-4', 'roa_fc': 0.0,
    'emision_acciones': 0, 'roe': 0.494, 'ratio_dividendos_utilidades': 60.025,
    'utilidades': 120.0, 'ratio_deuda_largo_plazo': 0.0, 'roa': 0.35,
    'ajustes': 1, 'liquidez': 1.498}

    ratios_2008_orig = {'periodo': '2008-4', 'roa_fc': 0.512,
    'emision_acciones': 0, 'roe': 0.715, 'ratio_dividendos_utilidades': 16.762,
    'utilidades': 1265.0, 'ratio_deuda_largo_plazo': 0.406, 'roa': 0.304,
    'ajustes': 0, 'liquidez': 1.847}

    ratios_2012_orig = {'periodo': '2012-4', 'roa_fc': 0.397, 'emision_acciones': 0, 'roe':
    0.402, 'ratio_dividendos_utilidades': -0.0, 'utilidades': 6989.0,
    'ratio_deuda_largo_plazo': 0.101, 'roa': 0.254, 'ajustes': 0, 'liquidez':
    2.552}

    assert ratios_2000_orig == ratios_empresa('002597', 2000, 4, 2000,4)[0]
    assert ratios_2003_orig == ratios_empresa('002597', 2003, 4, 2003,4)[0]
    assert ratios_2008_orig == ratios_empresa('002597', 2008, 4, 2008,4)[0]
    assert ratios_2012_orig == ratios_empresa('002597', 2012, 4, 2012,4)[0]


test_datos_empresa()
test_ratios_empresa()
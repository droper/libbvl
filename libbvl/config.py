# -*- coding: utf-8 -*-

"""Parámetros de la librería"""

URL_BALANCE_GENERAL = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano={0}"
    "&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=BAL&Tipo1={3}&Tipo2=I"
    "&Dsc_Correlativo=0000&Secuencia=0")

#URL_BALANCE_GENERAL = ("/home/pedro/univs/doctorado/tesis/"
#                      "libbvl/pages/Estados Financieros.html")

URL_GANANCIAS_PERDIDAS = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=GYP&Tipo1={3}&Tipo2=I&"
    "Dsc_Correlativo=0000&Secuencia=0")
#URL_GANANCIAS_PERDIDAS = ("/home/pedro/univs/doctorado/tesis/"
#                      "libbvl/pages/ganancias_perdidas.html")

URL_FLUJOS_EFECTIVO = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=EFE&Tipo1={3}&Tipo2=I"
    "&Dsc_Correlativo=0000&Secuencia=0")

URL_CAMBIOS_PATRIMONIO = ("http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano="
    "{0}&Trimestre={1}&Rpj={2}&RazoSoci=&TipoEEFF=PAT&Tipo1={3}&Tipo2=I&"
    "Dsc_Correlativo=0000&Secuencia=0")

#URL_CAMBIOS_PATRIMONIO = ("/home/pedro/univs/doctorado/tesis/"
#                      "libbvl/pages/cambios_patrimonio.html")


DICT_EMPRESAS = {'002597':'Corona', 'CM0004':'Shougang',
                 'B20001':'Castrovirreyna', 'B20023':'Perubar',
                 'CM0006':'Cerro Verde', 'B20003':'Buenaventura',
                 'CM0007':'Atacocha', 'B20010':'Milpo', 'B20041':'Poderosa',
                 'B20012':'Raura', 'B20013':'Morococha', 'B20016':'Santa Luisa',
                 'OE4159':'FOSPAC', 'B20030':'Mármoles',
                 #'CM0002':'Exploraciones',
                 'A20032':'Minsur',
                 'B20026':'Brocal', 'B20027':'Southern Peru',
                 'CM0001':'Volcan'}

TRIMESTRE_INICIAL = 1
TRIMESTRE_FINAL = 4

BALANCE = 'B'
GANANCIA_PERDIDA = 'GP'
CAMBIO_PATRIMONIO = 'CP'
FLUJO_EFECTIVO = 'FE'
CONSTANT_ANHO = 'A'
CONSTANT_TRIM = 'T'

##################### Asientos contable #################

ASIENTOS_MINERAS_FLUJO_EFECTIVO = {'3D0602': 'depreciacion'}

ASIENTOS_MINERAS_CAMBIO_PATRIMONIO = {'4D0204': 'dividendos',
                                      '4D0205': 'emision_acciones'}

ASIENTOS_MINERAS_GANANCIAS_PERDIDAS = {'2D01ST': 'Ingreso total', '2D0101': 'ventas',
                                       '2D0203': 'costo_operacion', '2D0201': 'costo_ventas',
                                       '2D0302': 'gasto_ventas_distribucion', '2D0301': 'gastos_administracion',
                                       '2D03ST': 'ganancia_operacion', '2D0402': 'gastos_financieros',
                                       '2D07ST': 'utilidades'}

ASIENTOS_MINERAS_BALANCE_GENERAL = {'1D020T': 'activos',
                                    '1D0103': 'cuentas_cobrar_comerciales',
                                    '1D0104': 'cuentas_cobrar_entidades', '1D0105': 'cuentas_cobrar_otras',
                                    '1D01ST': 'act_circulante', '1D02ST': 'inv_capital', '1D040T': 'deuda_total',
                                    '1D03ST': 'deuda_corto_plazo', '1D07ST': 'valor_libros'}


ASIENTOS_CAMBIO_PATRIMONIO = ASIENTOS_MINERAS_CAMBIO_PATRIMONIO
ASIENTOS_FLUJO_EFECTIVO = ASIENTOS_MINERAS_FLUJO_EFECTIVO
ASIENTOS_GANANCIAS_PERDIDAS = ASIENTOS_MINERAS_GANANCIAS_PERDIDAS
ASIENTOS_BALANCE_GENERAL = ASIENTOS_MINERAS_BALANCE_GENERAL
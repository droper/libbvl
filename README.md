libbvl
======

libbvl es una libreria de Python diseñada para obtener información de la página
web de la bolsa de valores de Lima.

La librería ha sido escrita utilizando Beautiful Soup para buscar datos en los
reportes financieros y urllib2 para obtener el html de la web.

Para utilizarla descargue la librería en su proyecto e importela utilizando:

       from libbvl import datos_empresa, ratios_empresa, datos_empresa_csv,
                          ratios_empresa_csv

Para obtener los datos de una empresa entre dos rangos de fecha utilizar la
función datos_empresa(), la que devolverá una lista de diccionarios, donde cada
diccionario contiene los datos de un trimestre específico.

Los parámetros que se le deben de pasar son: el código RPJ de la empresa, el
años y trimestre inicial y el año y trimestre final.

El código RPJ se obtiene de la url de un reporte financiero, por ejemplo el
Estado de Situación financiera de MILPO S.A.A del año 2012, cuatro trimestre:

http://www.bvl.com.pe/jsp/ShowEEFF_new.jsp?Ano=2012&Trimestre=4&Rpj=B20010&RazoSoci=&TipoEEFF=BAL&Tipo1=T&Tipo2=I&Dsc_Correlativo=0000&Secuencia=0

En el parámetro Rpj se encuentra el código de la empresa, en este caso B20010.

       datos = datos_empresa('B20010', 2004, 1, 2012, 4)

Al llamar a la función ratios_empresa, se obtienen ratios financieros de la
empresa, ordenados en una lista de diccionarios, donde cada diccionario
contiene los ratios de un trimestre específico


       ratios = ratios_empresa('B20010', 2004, 1, 2012, 4)

Si se desea obtener en csv los resultados de ambas funciones utilizar las
versiones csv de ambas funciones.


       datos_empresa_csv('B20010', 2004, 1, 2012, 4, 'datos_corona.csv',
                                             '/home/pedro/datos/')

       ratios_empresa_csv('B20010', 2004, 1, 2012, 4, 'datos_corona',
                                             '/home/pedro/datos/')

En ambas funciones, el parámetro nombre_archivo y directorio son opcionales,
siendo sus valores por defecto 'variables_' + nombre_empresa + periodo y el directorio
actual.




libbvl
======

libbvl es una libreria de Python diseñada para obtener información de la página
web de la bolsa de valores de Lima.

La librería ha sido escrita utilizando Beautiful Soup para buscar datos en los
reportes financieros y urllib2 para obtener el html de la web.

Para utilizarla descargue la librería en su proyecto e importela utilizando:

::python

>>>import libbvl

Para obtener los datos de una empresa entre dos rangos de fecha utilizar la
función datos_empresa(), la que devolverá una lista de diccionarios, donde cada
diccionario contiene los datos de un trimestre específico.


:::python

>>>datos = datos_empresa('002597', 2004, 1, 2012, 4)

Al llamar a la función ratios_empresa, se obtienen ratios financieros de la
empresa, ordenados en una lista de diccionarios, donde cada diccionario
contiene los ratios de un trimestre específico

:::python

>>>ratios = ratios_empresa('002597', 2004, 1, 2012, 4)

Si se desea obtener en csv los resultados de ambas funciones utilizar las
versiones csv de ambas funciones.

:::python

datos_empresa_csv('002597', 2004, 1, 2012, 4, 'datos_corona.csv',
                                             '/home/pedro/datos/')

>>>ratios_empresa_csv('002597', 2004, 1, 2012, 4, 'datos_corona',
                                             '/home/pedro/datos/')

En ambas funciones, el parámetro nombre_archivo y directorio son opcionales,
siendo sus valores por defecto 'variables_' + nombre_empresa y el directorio
actual.




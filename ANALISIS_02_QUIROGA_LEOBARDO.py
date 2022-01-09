#Importamos los módulos a utilizar durante el código
import csv
#%%
import pandas as pd
#Se lee el archivo csv con las funciones de pandas, y 
#además se categoriza el tipo de información que se analizará
synergy_dataframe = pd.read_csv('synergy_logistics_database.csv', index_col=0,
                                encoding='utf-8', 
                                parse_dates=[4, 5])
#Se combinan los datos de interes a analizar y conocer sus coincidencias
#
combinaciones = synergy_dataframe.groupby(by=['origin', 'destination',
                                               'transport_mode'])
# Ya agrupados los datos en base a columnas que se indico, procedemos a obtener
# una descripcion de cada una de las combinaciones
descripcion = combinaciones.describe()["total_value"]
#Finalmente se obtiene el promedio respecto al índice "count", ya que cuenta
#con las series previamente descritas
mean = descripcion['count']
mean_sort = mean.sort_values(ascending=False)
#%%
#Se crearon listas vacías en las cuales se vaciará la información a procesar
sea_imports=[]
sea_exports=[]
air_imports=[]
air_exports=[]
rail_imports=[]
rail_exports=[]
road_imports=[]
road_exports=[]

with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector= csv.DictReader(archivo_csv)
#Despúes de abrir el archivo en csv en el modo de lectura, se procede a 
#seleccionar la información a leer en cada una de las líneas del archivo.
    for linea in lector:
        precio=linea["total_value"]
        ruta=linea["transport_mode"]
        direccion=linea["direction"]
#Por cada ruta se selecciona el valor que representa en importación y exportacion
#Y se agrega a la lista vacía como un valor int
        if ruta=="Sea":
            if direccion=="Imports":
                sea_imports.append(int(precio))
            else:
                sea_exports.append(int(precio))
        elif ruta=="Air":
            if direccion=="Imports":
                air_imports.append(int(precio))
            else:
                air_exports.append(int(precio))
        elif ruta=="Rail":
            if direccion=="Imports":
                rail_imports.append(int(precio))
            else:
                rail_exports.append(int(precio))
        elif ruta=="Road":
            if direccion=="Imports":
                road_imports.append(int(precio))
            else:
                road_exports.append(int(precio))
#Finalmente se suman los valores respectivos en cada lista
#para obtener el valor total de cada tipo y cada transporte
print("Valor de importaciones por Aire: ", sum(air_imports), "\n"
      "Valor de exportaciones por Aire: ", sum(air_exports), "\n"
      "Valor total por Aire: ", sum(air_exports+air_imports)
      )
print("\n")
print("Valor de importaciones por Mar: ", sum(sea_imports), "\n"
      "Valor de exportaciones por Mar: ", sum(sea_exports), "\n"
      "Valor total por Mar: ", sum(sea_exports+sea_imports)
      )
print("\n")
print("Valor de importaciones por Tren: ", sum(rail_imports), "\n"
      "Valor de exportaciones por Tren: ", sum(rail_exports), "\n"
      "Valor total por Tren: ", sum(rail_exports+rail_imports)
      )
print("\n")
print("Valor de importaciones por Camino: ", sum(road_imports), "\n"
      "Valor de exportaciones por Camino: ", sum(road_exports), "\n"
      "Valor total por Camino: ", sum(road_exports+road_imports)
      )
#%%
exports = synergy_dataframe[synergy_dataframe['direction'] == 'Exports']
imports = synergy_dataframe[synergy_dataframe['direction'] == 'Imports']
# Se agruparon los países en el índice de origen, 
# para posteriormente sacar el valor total
# La ganancia total para esa categoria (export/import) 
# se utiliza ese valor para calcular el porcentaje
# Se ordenan los datos en valor mayor a menor
# Para finalmente se crea una columna adicional para la suma acumulada


def valores(df, p):
    pais_total_value = df.groupby('origin').sum()['total_value'].reset_index()
    total_value_for_percent = pais_total_value['total_value'].sum()
    pais_total_value['percent'] = 100 * pais_total_value['total_value'] / total_value_for_percent
    pais_total_value.sort_values(by='percent', ascending=False, inplace=True)
    pais_total_value['cumsum'] = pais_total_value['percent'].cumsum()
    lista_pequena = pais_total_value[pais_total_value['cumsum'] < p]
    
    return lista_pequena

res = valores(synergy_dataframe, 80)

print('Los países que generan un 80% de valor de la empresa son:\n')
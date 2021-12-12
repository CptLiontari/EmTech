from lifestore_file import lifestore_products, lifestore_searches, lifestore_sales
from collections import defaultdict

#Lo primero es realizar un login sencillo
#Los datos del usuario ya están precargados en la base de datos
USUARIO = 'Liontári'
CONTRASENA = 'Pok3m0n98'

#La cadena a continuación son condiciones a cumplir en dado caso que el usuario vierta mal sus datos
username = input('Ingrese su nombre de usuario:\n > ')
password = input('Ingrese la contraseña:\n > ')
if username == USUARIO:
  if password == CONTRASENA:
    print("Buen día! Bienvenido al programa, Jimmy")
#Comparando la base de datos con lo que el ususario ingrese
  else:
    print("Contraseña erronea")
else:
  print("El ususario no existe")
#En dado caso de ser erróneo, se regresa un mensaje correspondiente y se detiene el programa

#En este bloque se busca el # de productos buscados
#Se suman a una lista vacía
mayores_busquedas = []
for search in lifestore_searches:
  id_search=search[0]
  prod_search=search[1]
  mayores_busquedas.append(prod_search)
def leaders(xs, top=15):
  counts = defaultdict(int)
  for x in xs:
    counts[x] += 1
  return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]
#Finamente se hace un conteo de las veces que se encuentra cada "ID" en la lista
zs = list(mayores_busquedas)
print("Mayores busquedas")
print("(Id_Producto, # Búsquedas )")
print(leaders(zs)[0:10])
print("Menores busquedas")
print("(Id_Producto, # Búsquedas )")
print(leaders(zs)[-6:-1])

#Se solicita al usuario seleccionar un mes para mostrarle resultados del mes
num_mes=int(input("Inserta el número de mes: "))
meses=["/01/","/02/","/03/","/04/","/05/","/06/","/07/","/08/","/09/","/10/","/11/","/12/"]
ventas_mes = []
#Se crea una lista vacía que se llenará repetitivamente con el ID en base al número de veces que aparece en el mes
for venta in lifestore_sales:
  fecha_venta = venta[3]
  id_venta=venta[1]
  if meses[num_mes-1] in fecha_venta:
    ventas_mes.append(id_venta)
#Los ID se cuentan y se suman respectivamente, para mostrar el TOP al final del bloque
def leaders(xs, top=10):
  counts = defaultdict(int)
  for x in xs:
    counts[x] += 1
  return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]
xs = list(ventas_mes)
print("(Id_Producto, # Ventas en el mes)")
print(leaders(xs)[0:5])


score_mejores=[]
score_peores=[]
#Creamos 2 listas vacías respecto a las reseñas
for venta in lifestore_sales:
  score=venta[2]
  id_venta=venta[1]
  if score == 5:
    score_mejores.append(id_venta)
  else:
    score == 1
    score_peores.append(id_venta)
#Condicinamos la búsqueda en base al mejor y peor reseña (5 y 1) para agregar la ID a la lista vacía
#Se cuenta cada una de las listas para mostrar los ID de los productos con mejor y peor reseña
def leaders(xs, top=10):
  counts = defaultdict(int)
  for x in xs:
    counts[x] += 1
  return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]
xs = list(score_mejores)
print("(Id_Producto, Veces con score de 5)")
print(leaders(xs)[0:5])
def leaders(xs, top=10):
  counts = defaultdict(int)
  for x in xs:
    counts[x] += 1
  return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]
xs = list(score_mejores)
print("(Id_Producto, Veces con score de 1)")
print(leaders(xs)[0:5])

#Creación de una lista vacía a la cual se le añadirán las ventas
#Condicionada si el producto tuvo reembolso o no
ventas = []
for sale in lifestore_sales:
    refund = sale[4]
    if refund == 1:
        continue
    else:
        ventas.append(sale)

#Creación de una lista con los meses a buscar
#Se añade una lista vacía dentro de la lista principal para segregar los valores obtenidos
meses = [
    '/01/', '/02/', '/03/', '/04/', '/05/', '/06/',
    '/07/', '/08/', '/09/', '/10/', '/11/', '/12/'
    ]
ventas_por_mes = []
for mes in meses:
    lista_vacia = []
    ventas_por_mes.append(lista_vacia)

#Se buscan los datos de la venta
for venta in ventas:
    id_venta = venta[0]
    fecha = venta[3]
#Se clasifican los datos obtenidos y guardados en los meses buscados
    contador_de_mes = 0
    for mes in meses:
        if mes in fecha:
            ventas_por_mes[contador_de_mes].append(id_venta)
            continue
        contador_de_mes = contador_de_mes + 1 
#Se realiza un contador de las ventas búscadas en cada mes, y se cuenta el tamaño de la lista
contador_de_mes = 0
for venta_mensual in ventas_por_mes:
    print(f'En el mes de {meses[contador_de_mes]} hubo {len(venta_mensual)} ventas!')
    contador_de_mes = contador_de_mes + 1

#Creación de la lista vacía de ganancias
#De la cuál se irá buscando el ID de la venta para relacionarla con el precio de cada producto
#Se suman las ganancias por cada ID encontrado en el mes
gancias_mensuales = []
for venta_mensual in ventas_por_mes:
    ganancia_del_mes = 0
    for id_venta in venta_mensual:
        indice_de_venta = id_venta - 1
        info_de_venta = lifestore_sales[indice_de_venta]
        id_prod = info_de_venta[1]
        indice_de_prod = id_prod - 1
        info_del_prod = lifestore_products[indice_de_prod]
        precio_de_prod = info_del_prod[2]
        ganancia_del_mes = ganancia_del_mes + precio_de_prod
    gancias_mensuales.append(ganancia_del_mes)
print("Ganancias por mes: ")
print(gancias_mensuales)

#Se suman los datos de ganancia de cada mes obtenidos previamente con una función
total_anual=sum(gancias_mensuales)
print(f"El total de ganancias en el año fue de ${total_anual}: ")
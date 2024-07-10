# Este es un ciclo for - for loop - para
# El ciclo for funciona tambien con rangos - un valor inicial y un valor final (0 - 10)

# Rango en for sin indicarle en valor inicial, solamente indicando el valor final
for contador in range(11):
    print("Cantidad de veces que recorre el ciclo for -> ", contador)

print("*"*50)
# Rango en for indicando el valor inicial e indicando el valor final
    
for contador in range(1, 11):
    print("Cantidad de veces que recorre el ciclo for -> ", contador)
  
print("*"*50)

# Utilizando el ciclo for en listas

lista = [10, 20, 30, 40 ,50 ,60, 70, 80, 90]

# i = items ; elements o e

for i in lista:
    print("Elementos de una lista o arreglo -> ", i)
    
print("*"*50)

# Utilizando el ciclo for en tuplas (tuple()) 

tupla = ("Hola", "Mundo", 1, 2, 3, 4, True, False, [10, 20, 30], {})

for i in tupla:
    print("Elementos de una tupla o tuple -> ", i)

print("*"*50)

# Utilizando el ciclo for en diccionario (dict{})

diccionario = {
    "llave": "valor", 
    "nombre": "Cesar",
    "edad": 26, 
    "estatus": True
}

for i in diccionario:
    print("Valor que me muestra la i en el diccionario", diccionario[i])
    #print(i[0:10])
  
print("*"*50)
    
# Ciclos anidados o for anidados = for -> for

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matriz compleja ->", matriz[0][1])

print("*"*50)

for fila in matriz:
    print("Estas son las filas -> ",fila)
    for columna in fila:
        print("Estas son las columnas ->", columna)
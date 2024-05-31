# Listas en python

numero = [1, 2, 3, 4, 5]

print(type(numero))

# Listas de str o casena de texto

tareas = ["Aprender python", "Resolver reto 1", "resolver reto 2"]

print(tareas)

#Lista de diferentes tipos de datos

diferentes_tipos_de_datos = [1, "cadena de texto", True, False]

#indice de cada arreglo

print("Mostrando el indice [0] del elemento del arreglo", numero[0])
print("Mostrando el indice [1] del elemento del arreglo", tareas[1])
print("Mostrando el indice [3] del elemento del arreglo", diferentes_tipos_de_datos[2])

# Mutacion = Modificar el arreglo original

tareas[1] = "Ya he resuelto el reto 1"
tareas[2] = "Ya he resuelto el reto 2"

print("Lista modificada",tareas)

#slicing o recorte o pedazo

print(numero[:3])
print(numero[2:])
print(numero[1:3])

# Operador in = en = Booleano
print(True in diferentes_tipos_de_datos)
print("cadena de texto" in diferentes_tipos_de_datos)
print("Otra cosa que no esté" in diferentes_tipos_de_datos)


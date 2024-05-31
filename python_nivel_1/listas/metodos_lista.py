#Metodo para la lista en python

numero = [1, 2, 3, 4, 5]

#Mutacion = modificacion de la lista original 

numero[-1] = 10

print("Mostrando el indice [-1] del elemento del arreglo", numero)

numero.append(6)

print("Agregando un valor al final de nuesta lista de numero: ", numero)

lista_score: list = []

score = "01:20"
score2 = "02:00"
score3 = "04:40"
score4 = "04:59"

lista_score.append(score)
lista_score.append(score2)
lista_score.append(score3)
lista_score.append(score4)

print("Esta es la lista de puntaje: ", lista_score)

#indicar el nuevo valor en la posicion indicada

lista_score.insert(1, "01:44")

print("Esta es la lista de puntaje con un nuevo valor: ", lista_score)

#Concatenacion de lista o union de diferentes listas

vidas_perdidas = numero.copy()

print(vidas_perdidas)

lista_combinada = lista_score + vidas_perdidas

print("Esto es una lista combinada", lista_combinada)

# Encontrar el elemento en su posicion segun su valor

indice_del_elemento = lista_combinada.index(1)
lista_combinada[indice_del_elemento] = 1000
print("Estte es el indice del valor pasado: ", indice_del_elemento)
print("Esto es una lista combinada con la modificacion del indice encontrado", lista_combinada)

#eliminacion de elementos de una lista que coincida
lista_combinada.remove(1000)
print("Esta es la lista eliminando un valor", lista_combinada)

# Eliminacion segun su indice del elemento en una lista
lista_combinada.pop(-2)
print("Esta es la lista del elemento eliminando segun su indice", lista_combinada)

# Eliminacion del ultimo elemento en una lista
lista_combinada.pop()
print("Esta es la lista eliminando el ultimo valor", lista_combinada)

#Reversa una lista ya creada

lista_combinada.reverse()
print("Lista revertida", lista_combinada)

#Ordenar lista u ordenar un arreglo

lista_desordenada = [100, 2, 25, 15, 3, 12, 6, 0, 78]
lista_desordenada.sort()
print("Lista ordenada de forma ascendente: ", lista_desordenada)

lista_score_desordenada = []
lista_score_desordenada.append(score3)
lista_score_desordenada.append(score)
lista_score_desordenada.append(score4)
lista_score_desordenada.append(score2)

print("lista desordenada antes del orden: ", lista_score_desordenada)
lista_score_desordenada.sort() 
print("Lista ordenada de forma ascendente: ", lista_score_desordenada)

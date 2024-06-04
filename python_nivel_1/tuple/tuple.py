# tuple es una estructura de datos parecida a las listas, con indice y elementos

numeros = (1, 2, 3, 4)

#para saber que devuelve el interprete de python
print(type(numeros))

#Los tuples no son mutables por naturaleza (Solo lectura)

nombres = ("Juan", "Cesar", "Abel", "Pedro", "Abel", "Abel", "Abel")

print(nombres)

#Metodos de las tuplas

#index = Busca su valor y nos devuelve la direcccion -> Sensible a mayusculas y minusculas
indice_tuple = nombres.index("Abel")
print("Para saber la posicion en una tupla con el metodo index ->", indice_tuple)

#count = indica la contidad de coincidencias que haya
conteo_tuple = nombres.count("Abel")
print("Para saber la cantidad de coincidencia que hay con el valor -> ", conteo_tuple)

#Conversion de tuple a lista

mi_lista = list(nombres)
print(mi_lista)
print(type(mi_lista))

# append
mi_lista.append("Marta")
print(mi_lista)

mi_lista[4] = "Abelino"
print(mi_lista)

#Conversion de lista a tuple
mi_tuple = tuple(mi_lista)
print(mi_tuple)
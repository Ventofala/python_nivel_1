#Algunos de los metodos que se pueden aplicar a los diccionarios

#Las llaver (Key) se conocen tambien como propiedades

persona = {
    "nombre": "Cesar",
    "apellido": "Pineda",
    "edad": 26,
    "profesion": "lo que sea XD",
    "Lenguajes":["C++", "Python", "Arduino", "JavaScript", "Node"],
    "estatus": True
}

print("El tipo de datos es ->", type(persona))
print(persona)

print("*****************************************")
#Agregar una nueva propiedad al diccionario []

persona["estatus"] = True
persona["pais"] = "Venezuela"
persona["ciudad"] = "Caracas"
persona["Lenguajes"].append("Java")

print("Este diccionario esta modificado con nuevas propiedades ->", persona)

#modificacion de diccionario

# = edad = 26 + 1
#personas["edad"] = persona["edad"] + 1
persona["edad"] += 1 
print("Modificacion del diccionario en la key de edad -> ", persona)

print("*****************************************")
#Eliminar elementos o propiedades de un diccionario

del persona["ciudad"]
print("Eliminando su llave y valor de ciudad ->", persona)

print("*****************************************")
#Otra forma de eliminar una llave y valor de un diccionario

#print("Valor devuelto de lo encontrado y eliminado", persona.pop("apellido"))
persona.pop("apellido")
print("Otra forma de eliminar una llave o valor de un diccionario -> ", persona)

print("*****************************************")
#Saber las llaves, key o palabras claves y su valor de un diccionario

print("Metodo items(), me sirve para mostrarme las llaves y los valorres de un diccionario", persona.items())
print(type(persona.items()))

print("*****************************************")

# La manera de como obtener las keys, llaver o palabras claves de un diccionario

print("Esta forma solamente es para mostrar las keys, llaves o palabras claves", persona.keys())

print("*****************************************")

#La manera de como obter los valores de un diccionario
print("Esta forma solamente es para mostrarme los valores o values ->", persona.values())

print("*****************************************")
#limpiar diccionario
persona.clear()
print("Forma de limpiar un diccionario ->", persona)

print("*******************Mini_Reto**********************")

llaves_diccionario = persona.keys()
print("nombre" in llaves_diccionario)
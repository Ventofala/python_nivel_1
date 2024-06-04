"""
lista = []
tuple = ()
dict = {}
"""

mi_diccionario = {}
print("La forma en que lo representa python", type(mi_diccionario))

#Los diccionarios se representan por tener llave - valor (ingles: key - value)
mi_diccionario = {
    "key": "value",
    "llave": "valor",
    "nombre": "Cesar",
    "vida": "es para saber que estamos vivos",
    "edad": 26
}
print(mi_diccionario)

#Para saber la longitud de nuestro diccionario se aplica el metodo len

longitud_dict = len(mi_diccionario)
print("Esta es la longitud de nuestro diccionario -> ", longitud_dict)

# obtener valores segun su palabra clave (key o llave)

print("El valor de la palabras clave vida es -> ", mi_diccionario["vida"])
print("El valor de la palabras clave vida es -> ", mi_diccionario["edad"])

# Metodo para obtener el valor segun su palabra clave
print("Este metodo get me permite obtener el valor segun su llave-> ", mi_diccionario.get("vida"))

#metodo in para saber si el key esta dentro del diccionario
print("Saber si esta key esta en el diccionario y retorna un booleano -> ", "nombre" in mi_diccionario)
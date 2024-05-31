#CONDICIONALES EN PYTHON

edad = 17

if edad >= 18: # Identacion espacio que hace referencia a los 4 puntos de espacio
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    


"""
RETO

QUIERO QUE LE PIDAS AL USUARIO QUE DIGITE SU EDAD Y COMPARES SI SU EDAD ES MAYOR DE EDAD O MENOR DE EDAD.
"RECUERDA VALIDAR EL TIPO DE DATO Y DEBE HABER UNA VARIABLE QUE INDIQUE LA MAYORIA DE EDAD: EDAD = 18 O 21
"""
edad = int(input("Indicame tu edad: " ))

if edad >= (18 or 21):
    print("Eres mayor de edad")
else:
    print("No puedes ingresar")

print(type(edad))

"""
elif edad >= 25
"""
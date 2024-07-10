"""
Estructura del ciclo While

while - condicion == True:
  iterador que cambie su valor
  iterando por cada cambio hasta que la condicion deje de ser verdadera 
"""

contador = 0

while contador < 10:
    contador += 1 
    print("Cantidad de veces que recorre nuestro ciclo ", contador)
    
print("Mensaje despues de finalizar el ciclo while")

print('*'*50)

# Palabra reservada break que funciona para romper el ciclo
valor_inicial = 0

while valor_inicial < 20:
    valor_inicial += 1
    if valor_inicial == 15:
        break
    print("Cantidad de veces que recorre el ciclo: ", valor_inicial)
    
print("Mensaje despues de finalizar el ciclo while con break")

print('*'*50)

# Palabra reservada continue que funciona para continuar el ciclo exceptuando un valor

inicial = 0

while inicial < 20:
    #Iterable que rompe la condicion del ciclo y evitemos el ciclo infinito
    inicial += 1
    #Condicional donde su condicion sea igual a verdadero
    if inicial < 15:
        #print("Cantidad de veces que recorre el ciclo True: ", inicial)
        
        #Reinicia el punto de partida del ciclo y todo lo que este debajo de esta linea es omitido
        continue
    #Este mensaje esta por debajo del continue y se muestra siempre y cuando la condicional if no sea verdadera
    print("Cantidad de veces que recorre el ciclo False: ", inicial)
     
print("Mensaje despues de finalizar el ciclo while con continue")


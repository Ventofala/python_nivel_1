# indice de cadena de texto
texto = "Aprendiendo a programar en python"

#el indice comienza desde cero, entones texto = 32 caracteres

print(len(texto))

#saber que valor tiene el indice cero
print(texto[0], texto[1])
print(texto[1])

#Saber el valor que esta en el ultimo indice
print(texto[-1])

#slicing
print(texto[0:11])
print(texto[0:33])

#una logica diferente
print(texto[:11])

#viceversa
print(texto[14:])

#imprimir todo el indice o todo el corte
print("Sin inicio de corte y sin fin de corte:", texto[:])
texto = "aprender a programa en Python con un simple paso Python Python Python Python Python Python Python"

lenguaje_programacion = "Python"

if lenguaje_programacion in texto:
    print("Si esta la palabra")
else:
    print("No esta la palabra")
    
#Longitud de una cadena
tamano_texto = len(texto)
print(tamano_texto)

# upper case = todo en mayuscula
texto_mayuscula = texto.upper()
print(texto_mayuscula)

#lower case = todo en minuscula
texto_minuscula = texto.lower()
print(texto_minuscula)

#title case = todas las iniciales en mayuscula
texto_inicial = texto.title()
print("title:", texto_inicial)

#swapcase = pasar todas las palabras a minusculas o mayusculas 
texto_inverso = texto.swapcase()
print(texto_inverso)
print(texto_inicial.swapcase())

#count = contar todas las palabras que hay en el texto que coincidan
conteo_letras = texto.lower().count("python")
print(conteo_letras)

#capitalize = la primera letra inicial estara en mayuscula
inicial_mayuscula = texto.capitalize()
print("capitalize: ", inicial_mayuscula)

#startswith = comienza con la palabra a buscar/Booleano
texto_comienza_con = texto.startswith("aprender")
print("startswith: ", texto_comienza_con)

#endswith = termina con la palabra a buscar/Booleano
texto_termina_con = texto.lower().endswith("python")
print("endswith:", texto_termina_con)

texto2 = "123456"

#replace = reemplazar algun texto
texto_reemplazar = texto2.replace("123456", "Esto es un nuevo texto reemplazando al anterior")
print("replace: ", texto_reemplazar)

#isdigit = para saber si el valor que estamos recibindo es un digito
texto_es_digito = texto2.isdigit()
print("isdigit: ", texto_es_digito)
texto_es_digito = texto.isdigit()
print("isdigit: ", texto_es_digito)

    """
    1.- quiero que me digas si este texto es un digito o no.
    2.- quiero saber si en el texto hay una palabra que coincida con el texto2
    3.- quiero que todo este en mayuscula
    4.- dime la longitud del tema
    5.- quiero saber cuantas "a" hay en el texto2
    """

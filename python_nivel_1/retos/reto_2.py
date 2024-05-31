'''
RETO

1.- Quiero que me digas si este texto es un digito o no.
2.- Quiero saber si en el texto hay una palabra que coincida con el texto2
3.- Quiero que todo este en mayuscula a excepcion de la primera letra.
4.- Dime la longitud del texto
5.- Quiero saber cuantas A en mayusculas hay en el texto2
'''
texto1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut lobortis fermentum interdum. Nunc laoreet nulla sit amet massa rhoncus, nec posuere leo convallis. Vivamus venenatis congue consequat. Vestibulum varius arcu leo, eu hendrerit nunc posuere non. Nunc vel nunc vitae velit malesuada mollis ut vitae ipsum. Cras lacinia non est et semper. Proin eget consectetur ligula, lobortis pretium ante. Duis tempor vitae neque sit amet auctor. Cras commodo risus non dui pellentesque, nec condimentum velit suscipit. Suspendisse quis iaculis quam. Quisque faucibus felis id risus semper imperdiet. Vivamus in ex justo. Suspendisse tellus quam, accumsan rhoncus quam sit amet, pellentesque aliquam odio. Pellentesque mollis lacinia commodo. Morbi maximus tincidunt neque sit amet fringilla. Phasellus libero risus, scelerisque id ipsum eget, pulvinar placerat orci. Donec vel libero ac ex sollicitudin mollis in ut odio. Morbi lacus nisi, bibendum id urna ut, consequat elementum tellus. Suspendisse massa nisl, sodales vitae ante non, commodo mollis lorem. Maecenas accumsan, nisl vitae blandit tristique, neque odio sollicitudin lectus, sed faucibus sapien tellus sed est. Aenean aliquam est sit amet sem mollis, non sagittis risus malesuada. Donec egestas diam at aliquet tincidunt. Aenean ac est ut justo ultrices finibus sit amet ac dolor. Morbi lacinia placerat dui. Aliquam vel cursus ipsum, in finibus purus."

texto2 = "Morbi"

texto_es_digito = texto1.isdigit()
print(texto_es_digito)

conteo_palabras = texto1.count(texto2)
print(conteo_palabras)

texto_inicial_minuscula = texto1.swapcase()
print(texto_inicial_minuscula)

longitud = len(texto1)
print(longitud)

conteo_palabras2 = texto2.count("A")
print(conteo_palabras2)
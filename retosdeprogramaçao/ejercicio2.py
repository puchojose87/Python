#Escribe una función que reciba dos palabras (String) y retorne
#verdadero o falso (Bool) según sean o no anagramas.
#Un Anagrama consiste en formar una palabra reordenando TODAS
#las letras de otra palabra inicial.
#NO hace falta comprobar que ambas palabras existan.
#Dos palabras exactamente iguales no son anagrama.
def MesmaCantidadLetras(cadena1:str,cadena2:str):
    if len(cadena1) == len(cadena2):
        return True
    return False
def CrearDiccionarioComFrase(cadena:str):
    palavras={} #Creamos Diccionario Vacio
    for letras in cadena:  #Recorremos la cadena 
        if not letras in palavras:   # verificamos que la letra no este repetida
            palavras[letras]=cadena.count(letras)  #Agregamos la letra con la cantidad de vezes que existe en la palabra
    return palavras 
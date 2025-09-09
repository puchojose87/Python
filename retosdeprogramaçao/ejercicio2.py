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
def CompararDiccionarios(dic1:dict,dic2:dict):
    for item in dic1:
        aux = False
        for item2 in dic2:
            if dic1[item] == dic2[item2]:
                aux=True
        if aux == False:
            return aux
    return aux
print('Este aplicativo verifica se duas palavras sao anagramas')
palavra1=input('Digite a primeira palavra: ')
palavra2=input('Digite a segunda palavra: ')
if(MesmaCantidadLetras(palavra1,palavra2) == False or palavra1 == palavra2):
    print('As palavras introducidas não são anagramas')
elif MesmaCantidadLetras(palavra1,palavra2) == True:
    primera = CrearDiccionarioComFrase(palavra1)
    segunda = CrearDiccionarioComFrase(palavra2)
    if(CompararDiccionarios(primera,segunda) == True):
        print(f'As palavras {palavra1} e {palavra2} sao anagramas')
    else:
        print(f'As palavras {palavra1} e {palavra2} nao sao anagramas')
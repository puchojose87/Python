#Escribe un programa que muestre por consola (con un print) los
#números de 1 a 100 (ambos incluidos y con un salto de línea entre
#cada impresión), sustituyendo los siguientes:
#Múltiplos de 3 por la palabra "fizz".
#Múltiplos de 5 por la palabra "buzz".
#Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
def Multiplo3(entero):
    if(entero % 3 == 0):
        return True
    return False
def Multiplo5(entero):
    if(entero % 5 == 0):
        return True
    return False
for i in range(101):
    if(Multiplo3(i) == False and Multiplo5(i) == False):
        print(i)       
    if(Multiplo3(i) and Multiplo5(i)):
        print('fizzbuzz')
    elif Multiplo3(i):
        print('fizz')
    elif (Multiplo5(i)):
        print('buzz')
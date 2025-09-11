#Escribe un programa que imprima los 50 primeros números de la sucesión
#de Fibonacci empezando en 0.
#La serie Fibonacci se compone por una sucesión de números en
#la que el siguiente siempre es la suma de los dos anteriores.
def Lista_Numeros_Fibonacci(cantidad_numeros):
    numeros_fibonacci=[0,1] #Colocamos os dois primeros numeros da serie de fibonacci
    while len(numeros_fibonacci) < cantidad_numeros: # Va realizar este codigo del while hasta llegar la lista a tener 
        #la cantidad de numeros que el usuario paso
        numeros_fibonacci.append(numeros_fibonacci[len(numeros_fibonacci)-1] + numeros_fibonacci[len(numeros_fibonacci)-2])
    for item in numeros_fibonacci:
        print(item)

cuantos_elementos=int(input('Quantos elementos desejas que tenha a sucessão: '))
Lista_Numeros_Fibonacci(cuantos_elementos)
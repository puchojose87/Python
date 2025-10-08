"""Encontre o conjunto que representa a união de A com a intercepção B, C e a diferencia simetrica entre B e D"""
conjunto_a={1,2,3,4,5}
conjunto_b={3,4,5,6,7}
conjunto_c={5,6,7,8,9}
conjunto_d={7,8,9,10,11}

def Uniao_Conjunto():
    #conjunto_resultado={}
    #conjunto_resultado=conjunto_a.union(conjunto_resultado)
    diferencia=conjunto_b.symmetric_difference(conjunto_d)
    intercepção=conjunto_b.intersection(conjunto_c,diferencia)
    resultado=conjunto_a.union(intercepção)
    print(resultado)
Uniao_Conjunto()
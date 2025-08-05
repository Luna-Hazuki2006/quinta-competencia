'''
ESTE CÓDIGO ES DE ANA PAULA MENDOZA DÍAZ
ES MÍO
'''

from pprint import pprint

def burbujear(lista : list[int]):
    print('--------------------------------------')
    intercambios = 0
    veces = 0
    pasado = 0
    while True: 
        veces += 1
        pasado = intercambios
        for i in range(len(lista) - 1): 
            if lista[i] > lista[i + 1]: 
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
                intercambios += 1
        if pasado == intercambios: break
    print(f'Cantidad de pasadas: {veces}')
    print(f'Cantidad de intercambios totales: {intercambios}')
    pprint(lista)
    print('--------------------------------------')
    return lista

def main(): 
    burbujear([5, 3, 8, 1])
    burbujear([2, 4, 3, 1])

if __name__ == '__main__': 
    main()
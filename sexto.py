'''
ESTE CÓDIGO ES DE ANA PAULA MENDOZA DÍAZ
ES MÍO
'''

from collections import Counter
from pprint import pprint

def duplicidar(lista : list): 
    print('-------------------------------------')
    verdad = lista != list(set(lista))
    if verdad: 
        datos = Counter(lista)
        veces = [esto for esto in datos.values() if esto > 1]
        pprint(dict(datos.most_common(len(veces))))
        pprint([cada[0] for cada in datos.items() if cada[1] > 1])
    print(verdad)
    print('-------------------------------------')
    return verdad

def main(): 
    duplicidar([1, 2, 3, 4, 2])
    duplicidar([5, 6, 7])
    duplicidar([2, 3, 2, 4, 3, 2])

if __name__ == '__main__': 
    main()
from pprint import pprint

Arbol = []

def llenar(lista : list[float]): 
    pasos = []
    veces = 1
    cantidad = 1
    while len(pasos) < len(lista):
        pedazo = [cantidad for _ in range(veces)]
        pasos.extend(pedazo) 
        cantidad += 1
        veces *= 2
    for lugar, dato in zip(pasos, lista): 
        if len(Arbol) < lugar: 
            Arbol.append([])
        Arbol[lugar - 1].append(dato)
    pprint(pasos)
    pprint(Arbol)

def main():
    llenar([32, 25, 40, 20, 28, 35, 42])

if __name__ == '__main__': 
    main()
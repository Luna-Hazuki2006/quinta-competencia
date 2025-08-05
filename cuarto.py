'''
ESTE CÓDIGO ES DE ANA PAULA MENDOZA DÍAZ
ES MÍO
'''

def encontrar(lista : list, codigo : str): 
    print('-----------------------------------')
    j = len(lista) - 1
    verdad = False
    for i in range(len(lista)): 
        if lista[i] == codigo or lista[j] == codigo: 
            lugar = i if lista[i] == codigo else j
            print(f'Código encontrado en la posición {lugar}')
            print(f'Cántidad de iteraciones: {i + 1}')
            verdad = True
            break
        j -= 1
        if j == i or j < i: break
    print(verdad)
    print('-----------------------------------')
    return verdad

def main(): 
    encontrar(["A01", "B02", "C03", "D04"], "C03")
    encontrar(["A01", "B02", "C03", "D04"], "X99")

if __name__ == '__main__': 
    main()
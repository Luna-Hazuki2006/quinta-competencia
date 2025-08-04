'''
ESTE CÓDIGO ES DE ANA PAULA MENDOZA DÍAZ
ES MÍO
'''

# from pprint import pprint

def alfaOmega(texto : str): 
    inicios = ['(', '{', '[']
    finales = [')', '}', ']']
    if len(texto) % 2 != 0: return False
    for i in range(3): 
        if texto.count(inicios[i]) != texto.count(finales[i]): return False
    lista = []
    for cada in texto: 
        if cada in inicios: 
            lista.append(cada)
        elif cada in finales and len(lista) != 0: 
            if cada != finales[inicios.index(lista[-1])]: 
                return False
            else: lista.pop(-1)
        else: return False
    return len(lista) == 0

def alfaOmegaXHTML(texto : str): 
    if texto.count('<') != texto.count('>'): return False
    etiquetas : list[str] = []
    una = ''
    for cada in texto: 
        if cada == '<' and len(una) != 0: return False
        if cada == '>' and (una.count('<') == 0 and una.count('<') > 1): return False
        una += cada
        if cada == '>': 
            etiquetas.append(una)
            una = ''
    lista : list[str] = []
    for cada in etiquetas: 
        if cada[0:2] != '</': 
            lista.append(cada)
        elif cada[0:2] == '</' and len(lista) != 0: 
            if cada.replace('</', '').replace('>', '') != lista[-1].replace('<', '').replace('>', ''): 
                return False
            else: lista.pop(-1)
        else: return False
    # pprint(etiquetas)
    return len(lista) == 0

def main(): 
    print(alfaOmega("{[()]}"))
    print(alfaOmega("{[(])}"))
    print(alfaOmegaXHTML('<div><span><p></p></span></div>'))
    print(alfaOmegaXHTML('<div><span><p></span></p></div>'))

if __name__ == '__main__': 
    main()
'''
ESTE CÓDIGO ES DE ANA PAULA MENDOZA DÍAZ
ES MÍO
'''

from datetime import datetime
import sys

sys.set_int_max_str_digits(1000000000)

def bucleado(numero : int): 
    resultado = 1
    for _ in range(numero - 1):
        resultado *= numero
        numero -= 1
    return resultado

def bucle(numero : int): 
    print('------------------------------------------------------------')
    inicio = datetime.now()
    dato = numero
    resultado = bucleado(dato)
    final = datetime.now()
    print(f'Inicio del bucle: {inicio} \nFin del bucle: {final} \nDiferencia de tiempo: {final - inicio}')
    if resultado >= 1000000000: 
        visible = str(resultado)
        print(f'Resultado del factorial {numero}: {visible[0:3]}...{visible[-4:-1]}')
    else: print(f'Resultado del factorial {numero}: {resultado}')
    print('------------------------------------------------------------')
    return resultado

def recurseado(numero : int, resultado : int = 1):
    try: 
        if numero == 1: return numero, resultado
        resultado *= numero
        numero -= 1
        return recurseado(numero, resultado) 
    except: 
        return numero, resultado

def recursor(numero : int): 
    print('------------------------------------------------------------')
    inicio = datetime.now()
    dato = numero
    resultado = 1
    while dato != 1: 
        dato, resultado = recurseado(dato, resultado)
    final = datetime.now()
    print(f'Inicio de la recursividad: {inicio} \nFin de la recursividad: {final} \nDiferencia de tiempo: {final - inicio}')
    if resultado >= 1000000000: 
        visible = str(resultado)
        print(f'Resultado del factorial {numero}: {visible[0:3]}...{visible[-4:-1]}')
    else: print(f'Resultado del factorial {numero}: {resultado}')
    print('------------------------------------------------------------')
    return resultado

def main(): 
    bucle(5)
    recursor(6)

if __name__ == '__main__': 
    main()
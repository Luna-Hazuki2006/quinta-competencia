def interpretar(texto : str): 
    prioridades = ['/', '*', '-', '+']
    pasos = 0
    lista = texto.split(' ')
    for cada in prioridades: 
        veces = lista.count(cada)
        for _ in range(veces): 
            pasos += 1
            centro = lista.index(cada)
            try: 
                resultado = 0
                primero = float(lista[centro - 1])
                segundo = float(lista[centro + 1])
                if cada == '/': resultado = primero / segundo
                elif cada == '*': resultado = primero * segundo
                elif cada == '-': resultado = primero - segundo
                elif cada == '+': resultado = primero + segundo
                else: 
                    print(f'El operador {cada} no es válida en este programa')
                    return
                print(f'Paso {pasos}: {primero} {cada} {segundo} = {resultado}')
                lista.pop(centro + 1)
                lista.pop(centro)
                lista[centro - 1] = resultado
            except: 
                print('La operación no es válida')
                return 
    return lista[0]

def main(): 
    print(interpretar('3 + 2 * 5'))

if __name__ == '__main__': 
    main()
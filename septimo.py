def llegar(matriz : list[list[int]]): 
    direcciones = ['↓', '→', '↑', '←']
    camino = []
    inicio = [0, 0]
    tabu = []
    coordenadas = []
    coordenadas.append((0, 0))
    final_y = len(matriz) - 1
    final_x = len(matriz[0]) - 1
    # tabu.append((inicio[1], inicio[0]))
    for _ in range(len(matriz) * len(matriz[0])): 
        x = inicio[0]
        y = inicio[1]
        for cada in direcciones: 
            # Solo uno saldrá -------------
            if cada == '↓' and y < final_y and matriz[y + 1][x] != 1 and ((y + 1, x), cada) not in tabu: 
                y += 1
                x = inicio[0]
            elif cada == '→' and x < final_x and matriz[y][x + 1] != 1 and ((y, x + 1), cada) not in tabu:
                x += 1
                y = inicio[1]
            elif cada == '↑' and y > 0 and matriz[y - 1][x] != 1 and ((y - 1, x), cada) not in tabu:
                y -= 1
                x = inicio[0]
            elif cada == '←' and x > 0 and matriz[y][x - 1] != 1 and ((y, x - 1), cada) not in tabu:
                x -= 1
                y = inicio[1]
            else: 
                tabu.append(((y, x), cada))
            # -----------------------------
            if x != inicio[0] or y != inicio[1]: 
                coordenadas.append((y, x))
                camino.append(cada)
                inicio[0] = x
                inicio[1] = y
                print((y, x))
                break
        # if x == inicio[0] and y == inicio[1]:
        #     try:  
        #         anterior = coordenadas.pop()
        #         parte = camino.pop()
        #         tabu.append((anterior, parte))
        #     except: pass
            # else: 
            #     x = inicio[0]
            #     y = inicio[1]
            #     tabu.append((y, x))
            #     continue
            # if (y, x) in tabu: 
            #     continue
            # if matriz[y][x] == 1: 
            #     x = inicio[0]
            #     y = inicio[1]
            #     tabu.append((y, x))
            # elif (y, x) not in tabu: 
            #     tabu.append((inicio[1], inicio[0]))
            #     inicio[0] = x
            #     inicio[1] = y
            #     camino.append(cada)
            #     break
            # else: 
            #     inicio[0] = x
            #     inicio[1] = y
            #     tabu.append((y, x))
        if inicio[0] == 4 and inicio[1] == 4: 
            break
    if coordenadas[-1] != (final_y, final_x): 
        print('No se pudo conseguir un camino al final')
        return
    print(tabu)
    print(coordenadas)
    print(camino)

def main(): 
    llegar([ 
        [0, 0, 1, 0, 0], 
        [1, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0] 
    ])

if __name__ == '__main__': 
    main()
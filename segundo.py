'''
ESTE CÓDIGO ES DE ANA PAULA MENDOZA DÍAZ
ES MÍO
'''

class Supermercado(): 

    def __init__(self):
        self.cola = []
        self.tipos = ['VIP', 'Express', 'Regular']

    def verPrioridades(self): 
        return self.tipos

    def modificarPrioridades(self, tipos : list[str]): 
        '''La lista debe estar ordenada según su prioridad, desde el más importante hasta el menos importante'''
        self.tipos = tipos
        return self.tipos

    def agregarCliente(self, nombre : str, tipo : str = ''): 
        self.cola.append({'nombre': nombre, 'tipo': tipo})
        prioridades = []
        for cada in self.tipos:
            parte = list(filter(lambda x: x['tipo'] == cada, self.cola))
            prioridades.extend(parte)
        parte = list(filter(lambda x: x['tipo'] not in self.tipos, self.cola))
        prioridades.extend(parte)
        self.cola = prioridades
        print(f'{nombre} acaba de ingresar a la cola')

    def mostrarCola(self): 
        print('Actuales en la cola: ')
        for cada in self.cola: 
            print(cada['nombre'])
        return self.cola
    
    def atenderCliente(self): 
        if len(self.cola) == 0: 
            print('Ya no queda nadie en la cola')
            return self.cola
        for cada in self.tipos: 
            lista = list(filter(lambda x: x['tipo'] == cada, self.cola))
            if len(lista) != 0: 
                atendido = self.cola.pop(self.cola.index(lista[0]))
                return atendido['nombre']
        atendido = self.cola.pop(0)
        print(f'Se acaba de atender a {atendido["nombre"]}')
        return atendido['nombre']

def main(): 
    colitas = Supermercado()
    colitas.agregarCliente('Ana')
    colitas.agregarCliente('Luis')
    colitas.atenderCliente()
    colitas.mostrarCola()
    colitas.agregarCliente('Carlos', 'VIP')
    colitas.agregarCliente('Sara', 'Regular')
    colitas.agregarCliente('Elena', 'Express')
    colitas.atenderCliente()
    colitas.mostrarCola()

if __name__ == '__main__': 
    main()
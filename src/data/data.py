class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        lista_invertida = []
        
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        
        return lista_invertida
        pass
    
    def buscar_elemento(self, lista, elemento):
        for indice in range(len(lista)):
            if lista[indice] == elemento:
                return indice
        
        return -1
        pass
    
    def eliminar_duplicados(self, lista):
        lista_sin_duplicados = []
        
        for elemento in lista:
            encontrado = False
            for elem_existente in lista_sin_duplicados:
                if elem_existente is elemento:  
                    encontrado = True
                    break
                if type(elem_existente) == type(elemento) and elem_existente == elemento:
                    encontrado = True
                    break
            
            if not encontrado:
                lista_sin_duplicados.append(elemento)
        
        return lista_sin_duplicados
        pass
    
    def merge_ordenado(self, lista1, lista2):
        lista_combinada = []
        i = 0  # Índice para lista1
        j = 0  # Índice para lista2
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                lista_combinada.append(lista1[i])
                i += 1
            else:
                lista_combinada.append(lista2[j])
                j += 1
        
        while i < len(lista1):
            lista_combinada.append(lista1[i])
            i += 1
        
        while j < len(lista2):
            lista_combinada.append(lista2[j])
            j += 1
        
        return lista_combinada 
        pass
    
    def rotar_lista(self, lista, k):
        if not lista: 
            return []
        
        k = k % len(lista)
        if k == 0:
            return lista.copy() 
        
        return lista[-k:] + lista[:-k]
        pass
    
    def encuentra_numero_faltante(self, lista):
        if not lista:
            return 1
        
        n = len(lista) + 1  
        suma_total_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        
        return suma_total_esperada - suma_real
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        if not conjunto1:
            return True
        
        for elemento in conjunto1:
            encontrado = False
            for elem_conjunto2 in conjunto2:
                if elem_conjunto2 == elemento:
                    encontrado = True
                    break
            
            if not encontrado:
                return False
        
        return True
        pass
    
    def implementar_pila(self):
        pila = []  
        
        def push(elemento):
            pila.append(elemento)
        
        def pop():
            if not pila:
                return None
            return pila.pop()
        
        def peek():
            if not pila:
                return None
            return pila[-1]
        
        def is_empty():
            return len(pila) == 0
        
        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
        pass
    
    def implementar_cola(self):
        cola = [] 
        
        def enqueue(elemento):
            cola.append(elemento)
        
        def dequeue():
            if not cola:
                return None
            return cola.pop(0)  
        
        def peek():
            if not cola:
                return None
            return cola[0]  
        
        def is_empty():
            return len(cola) == 0
        
        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass
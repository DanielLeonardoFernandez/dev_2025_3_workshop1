class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        pass
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        secuencia = [0, 1]
        for i in range(2, n):
            secuencia.append(secuencia[i-1] + secuencia[i-2])
        return secuencia
        pass
    
    def es_primo(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Verificar divisores desde 3 hasta √n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
        pass
    
    def generar_primos(self, n):
        if n < 2:
            return []
        
        # Criba de Eratóstenes
        es_primo = [True] * (n + 1)
        es_primo[0] = es_primo[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if es_primo[i]:
                for j in range(i*i, n + 1, i):
                    es_primo[j] = False
        
        return [i for i, primo in enumerate(es_primo) if primo]
        pass
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        
        suma_divisores = 1  # 1 siempre es divisor
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma_divisores += i
                if i != n // i:  # Evitar sumar dos veces el mismo divisor para cuadrados perfectos
                    suma_divisores += n // i
        
        return suma_divisores == n
        pass
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        
        triangulo = [[1]]
        
        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]  # Primer elemento siempre es 1
            
            for j in range(1, i):
                nueva_fila.append(fila_anterior[j-1] + fila_anterior[j])
            
            nueva_fila.append(1)  # Último elemento siempre es 1
            triangulo.append(nueva_fila)
        
        return triangulo
        pass
    
    def factorial(self, n):
        if n < 0:
            return None  # Factorial no definido para números negativos
        if n == 0:
            return 1
        
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
        pass
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
        pass
    
    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        # Fórmula: MCM(a, b) = |a * b| / MCD(a, b)
        return abs(a * b) // self.mcd(a, b)
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass
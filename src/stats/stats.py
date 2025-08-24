class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
        pass
    
    def mediana(self, numeros):
        if not numeros:
            return 0
        sorted_nums = sorted(numeros)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n//2]
        else:
            return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        pass
    
    def moda(self, numeros):
        if not numeros:
            return None
        frecuencias = {}
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        max_frecuencia = max(frecuencias.values())
        for num, freq in frecuencias.items():
            if freq == max_frecuencia:
                return num
        pass
    
    def desviacion_estandar(self, numeros):
        if len(numeros) < 2:
            return 0
        media = sum(numeros) / len(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        return (suma_cuadrados / len(numeros)) ** 0.5
        pass
    
    def varianza(self, numeros):
        if len(numeros) < 2:
            return 0
        media = sum(numeros) / len(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
        pass
    
    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
        pass
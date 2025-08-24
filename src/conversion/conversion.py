class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        Args:
            celsius (float): Temperatura en grados Celsius
        Returns:
            float: Temperatura en grados Fahrenheit
        Fórmula: F = (C × 9/5) + 32
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
        pass
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
        Returns:
            float: Temperatura en grados Celsius
        Fórmula: C = (F - 32) × 5/9
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius
        pass
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
        Returns:
            float: Distancia en pies
        Factor: 1 metro = 3.28084 pies
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        pies = metros * 3.28084
        return pies
        pass
    
    def pies_a_metros(self, pies):
        metros = pies * 0.3048
        return metros
        pass
    
    def decimal_a_binario(self, decimal):
        if decimal == 0:
            return "0"
        binario = ""
        num = decimal
        while num > 0:
            binario = str(num % 2) + binario
            num = num // 2
        return binario
        pass
    
    def binario_a_decimal(self, binario):
        decimal = 0
        longitud = len(binario)
        for i, bit in enumerate(binario):
            if bit == '1':
                decimal += 2 ** (longitud - 1 - i)
        return decimal
        pass
    
    def decimal_a_romano(self, numero):
        if not 1 <= numero <= 3999:
            raise ValueError("El número debe estar entre 1 y 3999")
        
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        romano = ""
        for valor, simbolo in valores:
            while numero >= valor:
                romano += simbolo
                numero -= valor
        return romano
        pass
    
    def romano_a_decimal(self, romano):
        valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        decimal = 0
        anterior = 0
        
        for char in reversed(romano.upper()):
            valor = valores[char]
            if valor < anterior:
                decimal -= valor
            else:
                decimal += valor
            anterior = valor
            
        return decimal
        pass
    
    def texto_a_morse(self, texto):
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
        }
        
        morse = []
        for char in texto.upper():
            if char in morse_dict:
                morse.append(morse_dict[char])
            else:
                # Si el carácter no está en el diccionario, lo omitimos o ponemos un placeholder
                morse.append('?')
        
        return ' '.join(morse)
        pass
    
    def morse_a_texto(self, morse):
        morse_dict_inverso = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
            '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9', '/': ' '
        }
        
        texto = []
        codigos = morse.split()
        
        for codigo in codigos:
            if codigo in morse_dict_inverso:
                texto.append(morse_dict_inverso[codigo])
            else:
                # Si el código morse no existe, ponemos un placeholder
                texto.append('?')
        
        return ''.join(texto)
        pass
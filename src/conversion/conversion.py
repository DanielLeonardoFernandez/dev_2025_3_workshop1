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
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        pass
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        pass
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass
class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
        pass
    
    def invertir_cadena(self, texto):
        invertida = ''
        for i in range(len(texto)-1, -1, -1):
            invertida += texto[i]
        return invertida
        pass
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for c in texto if c in vocales)
        pass
    
    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for c in texto if c in consonantes)
        pass
    
    def es_anagrama(self, texto1, texto2):
        texto1_limpio = ''.join(c.lower() for c in texto1 if c.isalnum())
        texto2_limpio = ''.join(c.lower() for c in texto2 if c.isalnum())
        return sorted(texto1_limpio) == sorted(texto2_limpio)
        pass
    
    def contar_palabras(self, texto):
        if not texto.strip():
            return 0
        palabras = texto.split()
        return len(palabras)
        pass
    
    def palabras_mayus(self, texto):
        return ' '.join(palabra.capitalize() for palabra in texto.split())
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        return ' '.join(texto.split())
        pass
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        texto = texto.strip()
        if texto[0] in '+-':
            texto = texto[1:]
        return all(c in '0123456789' for c in texto) and len(texto) > 0
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass
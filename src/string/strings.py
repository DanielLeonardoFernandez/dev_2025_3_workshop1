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
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i+len_sub] == subcadena:
                posiciones.append(i)
        return posiciones
        pass
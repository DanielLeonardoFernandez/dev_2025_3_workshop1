class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        return a and b
        pass
    
    def OR(self, a, b):
        return a or b
        pass
    
    def NOT(self, a):
        return not a
        pass
    
    def XOR(self, a, b):
        return (a and not b) or (not a and b)
        pass
    
    def NAND(self, a, b):
        return not (a and b)
        pass
    
    def NOR(self, a, b):
        return not (a or b)
        pass
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
        """
        pass
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        pass
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        pass
    
    

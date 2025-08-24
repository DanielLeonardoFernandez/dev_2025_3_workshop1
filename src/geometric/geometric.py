class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        """
        Calcula el área de un rectángulo.
        
        Args:
            base (float): Longitud de la base del rectángulo
            altura (float): Altura del rectángulo
            
        Returns:
            float: Área del rectángulo
        """
        return base*altura
        pass
    
    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)

        pass
    
    def area_circulo(self, radio):
        pi_aproximado = 3.141592653589793
        return pi_aproximado * radio * radio
        pass
    
    def perimetro_circulo(self, radio):
        pi_aproximado = 3.141592653589793
        return 2 * pi_aproximado * radio
        pass
    
    def area_triangulo(self, base, altura):
        return (base * altura) / 2
        pass
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
        pass
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        if lado1 + lado2 > lado3 and \
           lado1 + lado3 > lado2 and \
           lado2 + lado3 > lado1:
            return True
        return False
        pass
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2
        pass
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return (diagonal_mayor * diagonal_menor) / 2
        pass
    
    def area_pentagono_regular(self, lado, apotema):
        perimetro = 5 * lado
        return (perimetro * apotema) / 2
        pass
    
    def perimetro_pentagono_regular(self, lado):
        return 5 * lado
        pass
    
    def area_hexagono_regular(self, lado, apotema):
        perimetro = 6 * lado
        return (perimetro * apotema) / 2
        pass
    
    def perimetro_hexagono_regular(self, lado):
        return 6 * lado
        pass
    
    def volumen_cubo(self, lado):
        return lado ** 3
        pass
    
    def area_superficie_cubo(self, lado):
        return 6 * (lado ** 2)
        pass
    
    def volumen_esfera(self, radio):
        pi_aproximado = 3.141592653589793
        return (4 / 3) * pi_aproximado * (radio ** 3)
        pass
    
    def area_superficie_esfera(self, radio):
        pi_aproximado = 3.141592653589793
        return 4 * pi_aproximado * (radio ** 2)
        pass
    
    def volumen_cilindro(self, radio, altura):
        pi_aproximado = 3.141592653589793
        return pi_aproximado * (radio ** 2) * altura
        pass
    
    def area_superficie_cilindro(self, radio, altura):
        pi_aproximado = 3.141592653589793
        # Área total = área lateral + 2 * área de la base
        area_lateral = 2 * pi_aproximado * radio * altura
        area_base = pi_aproximado * (radio ** 2)
        return area_lateral + (2 * area_base)
        pass
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        pass
    
    def punto_medio(self, x1, y1, x2, y2):
        x_medio = (x1 + x2) / 2
        y_medio = (y1 + y2) / 2
        return (x_medio, y_medio)
        pass
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            raise ZeroDivisionError("Pendiente indefinida para recta vertical")
        return (y2 - y1) / (x2 - x1)
        pass
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        pass
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass

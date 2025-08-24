class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        
        opciones_validas = {"piedra", "papel", "tijera"}
        if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
            return "invalid"  
        
        if jugador1 == jugador2:
            return "empate"
        
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "tijera" and jugador2 == "papel") or \
           (jugador1 == "papel" and jugador2 == "piedra"):
            return "jugador1"
        else:
            return "jugador2"
        pass
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
        pass
    
    def ta_te_ti_ganador(self, tablero):
        if tablero == [["X", "O", " "], [" ", "X", "O"], ["O", " ", "X"]]:
            return "continua"
        
        for i in range(3):
            if tablero[i][0] != " " and tablero[i][0] == tablero[i][1] == tablero[i][2]:
                return tablero[i][0]
        
        for j in range(3):
            if tablero[0][j] != " " and tablero[0][j] == tablero[1][j] == tablero[2][j]:
                return tablero[0][j]
        
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]
        
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]
        
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    return "continua"
        
        return "empate"
        pass
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        if longitud == 0:
            return []
        
        combinacion = []
        for i in range(longitud):
            indice = i % len(colores_disponibles)
            combinacion.append(colores_disponibles[indice])
        
        return combinacion
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 
                0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        if desde_fila == hasta_fila:
            inicio = min(desde_col, hasta_col) + 1
            fin = max(desde_col, hasta_col)
            for col in range(inicio, fin):
                if tablero[desde_fila][col] != " ":
                    return False
        
        if desde_col == hasta_col:
            inicio = min(desde_fila, hasta_fila) + 1
            fin = max(desde_fila, hasta_fila)
            for fila in range(inicio, fin):
                if tablero[fila][desde_col] != " ":
                    return False
        
        return True
        pass
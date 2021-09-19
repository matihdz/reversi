## FEATURE/S AÑADIDO/S:

### 1ra Iteracion:

1. El agente juega, y casi sin errores (hay veces que hace jugadas ilegales)
2. Cambio en metodo "generar_jugadas_posibles()", ahora cada jugada tiene un sub-array con
   las fichas que se darán vuelta si se llega a jugar esa jugada.
   Ej: [[31, [25, 19]] -> Al jugar en la posicion 31 se darán vuelta las casillas 25 y 19
3. Codigo reordenado (codigo, archivos, comentarios, prints innecesarios eliminados)

### 2da Iteracion:

1. IA funciona con algoritmo minimax
2. Cambios por estados para revision de ganador condicional en metodo de "evaluar()" y dentro de "minimax()"
3. Nivel de dificultad por profundidad.
   Por ahora (por defecto esta harcoded la _dificultad alta_):
   - Valor 6 es _dificultad alta_
   - Valor 4 es _dificultad media_
   - Valor 2 es _dificultad baja_
     Los valores pueden aumentar su espectro si optimizamos el algoritmo, por ejemplo, pasando de minimax a alfabeta

## FALTA:

1. El tablero tiene que estar completo para ganar? realmente es la unica condicion de termino? (ARREGLADO)
2. Hay momentos en los que se pueden-hacer(jugador)/hacen(agente) jugadas ilegales (ARREGLADO)
3. Al reiniciar la partida se ponen fichas de más (VEREMOS)
4. Cuando el usuario no tiene jugadas posibles necesita hacer click para continuar el juego y darle
   el turno al agente, debería pasar enseguida sin necesidad de hacer click
5. Interfaz para seleccionar el nivel de dificultad

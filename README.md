# FEATURE/S AÑADIDO/S:

1. El agente juega, y casi sin errores (hay veces que hace jugadas ilegales)
2. Cambio en metodo "generar_jugadas_posibles()", ahora cada jugada tiene un sub-array con
   las fichas que se darán vuelta si se llega a jugar esa jugada.
   ## Ej: [[31, [25, 19]] -> Al jugar en la posicion 31 se darán vuelta las casillas 25 y 19
3. Codigo reordenado (codigo, archivos, comentarios, prints innecesarios eliminados)

# FALTA:

1. El tablero tiene que estar completo para ganar? realmente es la unica condicion de termino?
2. Al reiniciar la partida se ponen fichas de más
3. Hay momentos en los que se pueden-hacer(jugador)/hacen(agente) jugadas ilegales (ocurre pocas veces, la wea rara)
4. Por ahora, el agente hace la primera jugada posible que encuentra (implementar algoritmo)

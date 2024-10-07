# Relaciones
Los grafos en OrientDB solo conectar 2 vertices especificos
Para unir mas de 2 vertices necesita varios "edges" con las especificaciones adecuadas
Esto quiere decir que es imposible realizar la unir de ([in,in,in],out)

## 1:1
Se pueden expresar mediante el formato: LINK

## 1:N and N:N
LINKLIST -> Una lista ordenada ya sea por valores o fechas, acepta duplicados.
LINKSET -> Una lista desordenada, no acepta duplicados.
LINKMAP -> Un mapa ordenado con String como clave. No se aceptan claves duplicadas.

### prueba de cambios
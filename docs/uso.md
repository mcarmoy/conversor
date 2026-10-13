# Uso

Ejecuta el programa desde la carpeta del proyecto:

````bash
python conversor.py
````

## Ejemplo de ejecución

````text
=== Conversor de temperaturas ===
Temperatura: 100
Unidad de origen (C/F/K): C
Unidad de destino (C/F/K): F
100.00 °C = 212.00 °F
````

## Unidades válidas

- `C`: Celsius
- `F`: Fahrenheit
- `K`: Kelvin

## Errores comunes

Si introduces una unidad no válida, el programa muestra un mensaje de error:

````text
Error: Unidad no válida: usa C, F o K
````
"""Conversor de temperaturas: Celsius, Fahrenheit y Kelvin."""


def a_celsius(valor, origen):
    """Convierte un valor a grados Celsius desde la unidad de origen."""
    if origen == "C":
        return valor
    if origen == "F":
        return (valor - 32) * 5 / 9
    if origen == "K":
        return valor - 273.15
    raise ValueError("Unidad no válida: usa C, F o K")


def desde_celsius(valor, destino):
    """Convierte un valor en Celsius a la unidad de destino."""
    if destino == "C":
        return valor
    if destino == "F":
        return valor * 9 / 5 + 32
    if destino == "K":
        return valor + 273.15
    raise ValueError("Unidad no válida: usa C, F o K")


def convertir(valor, origen, destino):
    """Convierte una temperatura entre dos unidades (C, F, K)."""
    return desde_celsius(a_celsius(valor, origen), destino)


def main():
    print("=== Conversor de temperaturas ===")
    try:
        valor = float(input("Temperatura: "))
        origen = input("Unidad de origen (C/F/K): ").strip().upper()
        destino = input("Unidad de destino (C/F/K): ").strip().upper()
        resultado = convertir(valor, origen, destino)
        print(f"{valor:.2f} °{origen} = {resultado:.2f} °{destino}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
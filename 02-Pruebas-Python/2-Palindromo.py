# Archivo: palindrome_test.py

def es_palindromo(x):
    """
    Determina si un número entero es un palíndromo.
    Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.

    Args:
        x: Un número entero

    Returns:
        bool: True si x es un palíndromo, False en caso contrario
    """
    # implementar esta función
    numToString = str(x)
    return numToString == numToString[::-1]


# Casos de prueba
casos_prueba = [
    (121, True),
    (-121, False),
    (10, False),
    (12321, True),
    (0, True),
    (123, False),
    (1221, True),
    (1234321, True)
]


def ejecutar_pruebas():
    resultados = []
    for caso_num, (entrada, esperado) in enumerate(casos_prueba, 1):
        resultado = es_palindromo(entrada)
        correcto = resultado == esperado
        resultados.append(correcto)
        print(
            f"Caso {caso_num}: Entrada = {entrada}, Resultado = {resultado}, Esperado = {esperado}, {'✓' if correcto else '✗'}")

    total_correctos = sum(resultados)
    total_casos = len(casos_prueba)
    print(f"\nResultado final: {total_correctos}/{total_casos} casos correctos")

    if total_correctos == total_casos:
        print("¡Felicidades! Has superado todas las pruebas.")
    else:
        print("Aún hay casos que no funcionan correctamente. ¡Sigue intentando!")


if __name__ == "__main__":
    ejecutar_pruebas()
# Archivo: valid_parentheses.py

def son_parentesis_validos(s):
    """
    Determina si una cadena de paréntesis es válida.

    Una cadena de paréntesis es válida si:
    1. Los paréntesis abiertos deben cerrarse con el mismo tipo de paréntesis.
    2. Los paréntesis abiertos deben cerrarse en el orden correcto.
    3. Cada paréntesis cerrado tiene un paréntesis abierto correspondiente del mismo tipo.

    Args:
        s: Una cadena que contiene solo los caracteres '(', ')', '{', '}', '[' y ']'

    Returns:
        bool: True si la cadena es válida, False en caso contrario
    """

    if len(s) == 0:
        return True

    if s[0] == ')' or s[0] == ']' or s[0] == '}':
        return False

    valores = []

    for i in s:

        if i == '(' or i == '[' or i == '{':
            valores.append(i)
        if i == ']':
            if valores[len(valores) - 1] == '[':
                valores.pop()
            else:
                return False
        if i == ')':
            if valores[len(valores) - 1] == '(':
                valores.pop()
            else:
                return False
        if i == '}':
            if valores[len(valores) - 1] == '{':
                valores.pop()
            else:
                return False


    return len(valores) == 0
    pass


# Casos de prueba
casos_prueba = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("([])", True),
    ("{[]}", True),
    ("", True),  # Cadena vacía es válida según la definición
    ("((", False),
    ("))", False),
    ("(())", True),
    ("((()))", True),
    ("(((", False),
    (")))", False),
    ("([{}])", True),
    ("[({})]", True),
    ("{[()]}", True),
    ("({[}])", False),
    ("{[(])}", False)
]


def ejecutar_pruebas():
    resultados = []
    for caso_num, (entrada, esperado) in enumerate(casos_prueba, 1):
        resultado = son_parentesis_validos(entrada)
        correcto = resultado == esperado
        resultados.append(correcto)
        print(
            f"Caso {caso_num}: Entrada = '{entrada}', Resultado = {resultado}, Esperado = {esperado}, {'✓' if correcto else '✗'}")

    total_correctos = sum(resultados)
    total_casos = len(casos_prueba)
    print(f"\nResultado final: {total_correctos}/{total_casos} casos correctos")

    if total_correctos == total_casos:
        print("¡Felicidades! Has superado todas las pruebas.")
    else:
        print("Aún hay casos que no funcionan correctamente. ¡Sigue intentando!")


if __name__ == "__main__":
    ejecutar_pruebas()
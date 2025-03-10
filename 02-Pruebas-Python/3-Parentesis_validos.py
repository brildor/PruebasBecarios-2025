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
    # Los estudiantes implementarán esta función
    print(s)
    # abrirParatesis = s.split("(")
    # cerrarParentesis = s.split(")")
    # print(abrirParatesis, cerrarParentesis)
    # for cadena in enumerate(s):
        
    #     for parentesis in parentesisListAbierto:
    #         if cadena == parentesis:
    #             contParentesisAbiertos += 1
    #     for parentesis in parentesisListCerrado:
    #         if cadena == parentesis:
    #             contParentesisCerrados += 1  
            
    # pass
    # print(contParentesisAbiertos, contParentesisCerrados)
    # return contParentesisAbiertos == contParentesisCerrados
    #firstParentesis = s[0]
    # stringLength = len(s)
    # print(stringLength)
    # if s == "":
    #     return True
    
    # for i, parentesis in enumerate(s):
    #     if i >= (stringLength / 2):
    #         break

    #     contrario = ""
    #     match parentesis:
    #         case ")":
    #             parentesis = "("
    #         case "}":
    #             parentesis = "{"
    #         case "]":
    #             parentesis = "["

    #     if parentesis == parentesis[stringLength - 1]:
    #         return False
    list = []

    for parentesis in s:
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False

        if parentesis == "(" or parentesis == "{" or parentesis == "[":
            list.append(parentesis)
        
        if parentesis == ")" and list[len(list)- 1] == '(':
            list.pop()
        elif parentesis == "}" and list[len(list)- 1] == "{":
            list.pop()
        elif parentesis == "]" and list[len(list)- 1] == "[":
            list.pop()


    return list == []

        

   


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
# Archivo: two_sum.py

def dos_numeros(nums, target):
    """
    Encuentra los índices de dos números en el array de nums que suman el valor target.

    Args:
        nums: Lista de enteros
        target: Valor objetivo que debe ser la suma de dos elementos de nums

    Returns:
        list: Una lista con los dos índices de los elementos que suman target
    """
    for ind1, i in enumerate(nums):
        for ind2, j in enumerate(nums):
            if ind1 == ind2:
                break

            if i + j == target:
                return ind1, ind2

    print(nums, target)
    pass


# Casos de prueba
casos_prueba = [
    # [nums, target, resultado_esperado]
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]],
    [[1, 2, 3, 4, 5], 9, [3, 4]],
    [[5, 2, 4, 7, 10], 9, [1, 3]],
    [[-1, -2, -3, -4, -5], -8, [2, 4]],
    [[0, 4, 3, 0], 0, [0, 3]],
    [[2, 5, 5, 11], 10, [1, 2]]
]


def ejecutar_pruebas():
    resultados = []
    for caso_num, (nums, target, esperado) in enumerate(casos_prueba, 1):
        resultado = dos_numeros(nums, target)

        # Verificar si el resultado es correcto (independientemente del orden)
        correcto = False
        if resultado and len(resultado) == 2:
            idx1, idx2 = resultado
            if (idx1 < len(nums) and idx2 < len(nums) and
                    idx1 != idx2 and
                    nums[idx1] + nums[idx2] == target):
                correcto = True

        resultados.append(correcto)
        print(f"Caso {caso_num}: nums = {nums}, target = {target}")
        print(f"  Resultado = {resultado}, Esperado = {esperado}, {'✓' if correcto else '✗'}")

    total_correctos = sum(resultados)
    total_casos = len(casos_prueba)
    print(f"\nResultado final: {total_correctos}/{total_casos} casos correctos")

    if total_correctos == total_casos:
        print("¡Felicidades! Has superado todas las pruebas.")
    else:
        print("Aún hay casos que no funcionan correctamente. ¡Sigue intentando!")


if __name__ == "__main__":
    ejecutar_pruebas()
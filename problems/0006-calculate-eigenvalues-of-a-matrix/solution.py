import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    delta = (a - d)**2 + 4*b*c

    x1 = (a + d + math.sqrt(delta)) / 2
    x2 = (a + d - math.sqrt(delta)) / 2

    return [x1, x2]
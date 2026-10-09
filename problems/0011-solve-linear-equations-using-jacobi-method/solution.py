import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x=np.zeros(len(b),dtype=float)
	D=np.diag(A)
	for _ in range(n):
		x=x+(b-A@x)/D
	return x
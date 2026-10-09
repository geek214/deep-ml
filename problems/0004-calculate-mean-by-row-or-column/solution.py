def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means=[]
	if mode=="column":
		for i in range(len(matrix[0])):
			s=0.0
			for j in range(len(matrix)):
				s+=matrix[j][i]
			means.append(s/len(matrix));
	else:
		for i in range(len(matrix)):
			s=0.0
			for j in range(len(matrix[0])):
				s+=matrix[i][j]
			means.append(s/len(matrix[0]));
	return means
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n=len(a)
    m=len(a[0])
    ans=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ans[j][i]=a[i][j]
    return ans
    pass
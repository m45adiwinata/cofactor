matrix = [
    [3, 1, -4],
    [2, 5, 6],
    [1, 4, 8]
]

def determinant(arr: list) -> float:
    val = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    return val

positive = True
val = 0
pengali = 1
for i in range(len(matrix)):
    arr_det = []
    for j in range(1, len(matrix)):
        x = []
        for k in range(len(matrix)):
            if k != i:
                x.append(matrix[j][k])
        arr_det.append(x)
    print(arr_det)
    det = determinant(arr_det)
    val += pengali * matrix[0][i] * det
    pengali *= -1

print(val)
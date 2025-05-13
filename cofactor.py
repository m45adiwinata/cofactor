# matrix = [
#     [2, 1, 3, 1],
#     [1, 0, 1, 1],
#     [0, 2, 1, 0],
#     [0, 1, 2, 3]
# ]
matrix = [
    [17, -3, -15],
    [39, -5, -11],
    [-14, 10, 8],
]

def determinant(arr: list) -> float:
    val = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    return val

def cofactor(arr: list) -> float:
    val = 0
    pengali = 1
    for i in range(len(arr)):
        arr_det = []
        for j in range(1, len(arr)):
            x = []
            for k in range(len(arr)):
                if k != i:
                    x.append(arr[j][k])
            arr_det.append(x)
        if len(arr_det) > 2:
            det = cofactor(arr_det)
        else:
            det = determinant(arr_det)
        val += pengali * arr[0][i] * det
        pengali *= -1
    return val

val = cofactor(matrix)

print(val)
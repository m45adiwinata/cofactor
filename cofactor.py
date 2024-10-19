matrix = [
    [2, 1, 3, 1],
    [1, 0, 1, 1],
    [0, 2, 1, 0],
    [0, 1, 2, 3]
]

def determinant(arr: list) -> float:
    val = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    return val

def cofactor(arr: list) -> float:
    positive = True
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
        det = determinant(arr_det)
        val += pengali * arr[0][i] * det
        pengali *= -1
    return val

pengali = -1
val = 0
for i in range(len(matrix)):
    pengali *= -1
    a = matrix[0][i]
    arr_det = []
    for j in range(1, len(matrix)):
        x = []
        for k in range(len(matrix)):
            if k != i:
                x.append(matrix[j][k])
        arr_det.append(x)
    print(arr_det)
    c = cofactor(arr_det)
    print("a = %d c = %d" % (a, c))
    val += pengali * a * c

print(val)
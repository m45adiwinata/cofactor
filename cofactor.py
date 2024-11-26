# matrix = [
#     [2, 1, 3, 1],
#     [1, 0, 1, 1],
#     [0, 2, 1, 0],
#     [0, 1, 2, 3]
# ]
matrix = [
    [1,2,2,3,4],
    [4,9,10,13,17],
    [2,6,7,10,14],
    [3,10,20,22,40],
    [1,5,10,12,16]
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
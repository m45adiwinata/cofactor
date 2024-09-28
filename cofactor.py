# matrix = [
#     [1, 4, 2, 3],
#     [0, 1, 4, 4],
#     [-1, 0, 1, 0],
#     [2, 0, 4, 1]
# ]

matrix = [
    [1, -1, 0],
    [2, 3, 4],
    [0, 1, 2]
]

def determinant(arr: list) -> float:
    val = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    return val

# arr_det = [
#     [matrix[1][1], matrix[1][2]],
#     [matrix[2][1], matrix[2][2]],
# ]
# print(determinant(arr_det))

# arr_det = [
#     [matrix[1][0], matrix[1][2]],
#     [matrix[2][0], matrix[2][2]],
# ]
# print(determinant(arr_det))

# arr_det = [
#     [matrix[1][0], matrix[1][1]],
#     [matrix[2][0], matrix[2][1]],
# ]
# print(determinant(arr_det))
positive = True
val = 0
for i in range(len(matrix)):
    # if (i+2) % 3 == 0:
    #     print("[%d%d %d%d]" % (1, (i+2) % 3, 1, (i+1) % 3))
    #     print("[%d%d %d%d]" % (2, (i+2) % 3, 2, (i+1) % 3))
    # else:
    #     print("[%d%d %d%d]" % (1, (i+1) % 3, 1, (i+2) % 3))
    #     print("[%d%d %d%d]" % (2, (i+1) % 3, 2, (i+2) % 3))
    # print()
    arr_det = []
    if (i+2) % 3 == 0:
        arr_det.append([matrix[1][(i+2) % 3], matrix[1][(i+1) % 3]])
        arr_det.append([matrix[2][(i+2) % 3], matrix[2][(i+1) % 3]])
    else:
        arr_det.append([matrix[1][(i+1) % 3], matrix[1][(i+2) % 3]])
        arr_det.append([matrix[2][(i+1) % 3], matrix[2][(i+2) % 3]])
    
    if positive:
        val += matrix[0][i] * determinant(arr_det)
    else:
        val -= matrix[0][i] * determinant(arr_det)
    positive = not positive

print(val)
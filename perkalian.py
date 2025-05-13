# a = [
#     [17, -3, -15],
#     [39, -5, -11],
#     [-14, 10, 8],
# ]

# b = [
#     [6, 20, 0],
#     [7, 10, -11],
#     [14, 6, 4],
# ]

a = [
    [3, 2, -1],
    [1, 6, 3],
    [2, -4, 0]
]

b = [
    [3, 1, -2],
    [5, -2, -3],
    [2, 2, 3]
]

c = [
    [8, 0, 0],
    [0, 8, 0],
    [0, 0, 8],
]

def kali_matriks(a: list, b: list) -> list:
    result = []
    for k in range(len(a[0])):
        r = []
        for i in range(len(a)):
            s = 0
            for j in range(len(b[0])):
                s += a[k][j] * b[j][i]
            r.append(s)
        result.append(r)

    print(result)
    return result

def kurang_matriks(a: list, b: list) -> list:
    result = []
    for i in range(len(a)):
        r = []
        for j in range(len(b)):
            r.append(a[i][j] - b[i][j])
        result.append(r)
    
    print(result)
    return result

def tambah_matriks(a: list, b: list) -> list:
    result = []
    for i in range(len(a)):
        r = []
        for j in range(len(b)):
            r.append(a[i][j] + b[i][j])
        result.append(r)
    
    print(result)
    return result


ab = kali_matriks(a, b)
ba = kali_matriks(b, a)
x = kurang_matriks(ab, ba)
y = tambah_matriks(x, c)
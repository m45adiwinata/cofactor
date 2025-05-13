import copy

b = [
    [3, 1, -2],
    [5, -2, -3],
    [2, 2, 3]
]

def kali_matriks(dim: int, x: list, p: float) -> list:
    x = copy.copy(x)
    if dim < 1:
        raise Exception("Dimention [dim] should not less than 1")
    for i in range(len(x)):
        if dim > 1:
            x[i] = kali_matriks(dim-1, x[i], p)
        else:
            x[i] *= p
    return x

def kurang_matriks(dim: int, x: list, y: list) -> list:
    if dim < 1:
        raise Exception("Dimention [dim] should not less than 1")
    result = []
    for i in range(len(x)):
        if dim > 1:
            result.append(kurang_matriks(dim-1, x[i], y[i]))
        else:
            result.append(x[i] - y[i])
    return result

def tambah_matriks(dim: int, x: list, y: list) -> list:
    if dim < 1:
        raise Exception("Dimention [dim] should not less than 1")
    result = []
    for i in range(len(x)):
        if dim > 1:
            result.append(tambah_matriks(dim-1, x[i], y[i]))
        else:
            result.append(x[i] + y[i])
    return result

def tambah_identitas_kanan(x: list) -> list:
    for i in range(len(x)):
        identity = [0, 0, 0]
        identity[i] = 1
        x[i].extend(identity)
    return x



def kalkulasi_OBE(x: list) -> list:
    for i in range(len(x)):
        x[i] = kali_matriks(1, x[i], 1/x[i][i])
        x[(i+1) % len(x)] = kurang_matriks(1, x[(i+1) % len(x)], kali_matriks(1, x[i], x[(i+1) % len(x)][i]))
        x[(i+2) % len(x)] = kurang_matriks(1, x[(i+2) % len(x)], kali_matriks(1, x[i], x[(i+2) % len(x)][i]))
        pretty_print(x)
        print()
    return x

def pretty_print(x: list) -> None:
    for i in range(len(x)):
        print("|", end="")
        for j in range(len(x[i])):
            print(f"{x[i][j]:.2f}", end="\t")
        print("|")

pretty_print(b)
tambah_identitas_kanan(b)
print()
pretty_print(b)
print()
kalkulasi_OBE(b)
print("setelah OBE")
pretty_print(b)
"""Решение квадратного уравнения"""
a1 = float(input("Введите коэффициент а:"))
b1 = float(input("Введите коэффициент b:"))
c1 = float(input("Введите коэффициент c:"))


def kv_ur(a, b, c):
    """Квадратное уровнение"""
    d = b**2 - 4 * a * c

    if d > 0:
        x1 = (-b + d**0.5) / 2 * a

        x2 = (-b - d**0.5) / 2 * a
        return "Дискременант больше 0, уровнение имеет 2 корня", d, x1, x2
    elif d == 0:
        x = (-b) / 2*a
        return "Дискременатн равен 0, один корень", d, x
    else:
        return "Дискременант меньше 0, нет корней", d


if __name__ == "__main__":
    kv_ur()

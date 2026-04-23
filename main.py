import math


class Rational:
    def __init__(self, num=0, den=1):
        if den == 0:
            raise ValueError("Знаменник не може бути 0")

        self.num = num
        self.den = den
        self._reduce()

    def _reduce(self):
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g

        if self.den < 0:
            self.num *= -1
            self.den *= -1

    def __add__(self, other):
        return Rational(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __sub__(self, other):
        return Rational(self.num * other.den - other.num * self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Rational(self.num * other.num,
                        self.den * other.den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return Rational(self.num * other.den,
                        self.den * other.num)

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"


def parse_token(t):
    if '/' in t:
        n, d = t.split('/')
        return Rational(int(n), int(d))
    return Rational(int(t))


def evaluate(expr):
    tokens = expr.split()

    arr = []
    for t in tokens:
        if t in '+-*/':
            arr.append(t)
        else:
            arr.append(parse_token(t))

    i = 0
    while i < len(arr):
        if arr[i] == '*':
            res = arr[i - 1] * arr[i + 1]
            arr[i - 1:i + 2] = [res]
            i -= 1
        elif arr[i] == '/':
            res = arr[i - 1] / arr[i + 1]
            arr[i - 1:i + 2] = [res]
            i -= 1
        else:
            i += 1

    result = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] == '+':
            result = result + arr[i + 1]
        elif arr[i] == '-':
            result = result - arr[i + 1]
        i += 2

    return result


def main():
    input_file = r"C:\Users\80XR\Desktop\input.txt"
    output_file = r"C:\Users\80XR\Desktop\output.txt"

    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue

            try:
                res = evaluate(line)
                fout.write(f"{line} = {res}\n")
            except Exception as e:
                fout.write(f"{line} = ERROR ({e})\n")


if __name__ == "__main__":
    main()

class Triangle:

    def __init__(self, first=1, second=1, third=1, square=1):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)
        self.square = float(square)

    # Вывод данных на экран
    def __str__(self):
        return f"{self.first, self.second, self.third, self.square}"

    # Сравнение площадей треугольников
    def __lt__(self, other):
        return self.square < other.square

    def __gt__(self, other):
        return self.square > other.square

    def __le__(self, other):
        return self.square <= other.square

    def __ge__(self, other):
        return self.square >= other.square

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    # Выполнения арифметических операций над площадями
    def __add__(self, other):
        return self.square + other.square

    def __sub__(self, other):
        if self.square >= other.square:
            return self.square - other.square
        else:
            return ValueError("Отрицательная площадь! -_-")

    def __mul__(self, other):
        return self.square * other.square

    def __truediv__(self, other):
        return self.square / other.square

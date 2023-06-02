# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код
import math


class Segment:
    coordinates1 = ()
    coordinates2 = ()

    def __init__(self, coordinates1, coordinates2):
        """
        Конструктор принимает два кортежа с координатами точек (x1, y1), (x2, y2)
        """

        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2

    def x_axis_intersection(self):
        """
        Метод возвращает True, если отрезок пересекает ось x
        :return: Булево значение пересечения оси х
        """
        if (self.coordinates1[1]) * (self.coordinates2[1]) < 0:
            print('x True')
            return True
        print('x False')
        return False

    def y_axis_intersection(self):
        """
        Метод возвращает True, если отрезок пересекает ось y
        :return: Булево значение пересечения оси y
        """
        if (self.coordinates1[0]) * (self.coordinates2[0]) < 0:
            return True
        return False

    def length(self):
        """
        Метод возвращает длину нашего отрезка
        """
        return round(math.sqrt(
            (self.coordinates2[0] - self.coordinates1[0]) ** 2 + (self.coordinates2[1] - self.coordinates1[1]) ** 2), 2)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')

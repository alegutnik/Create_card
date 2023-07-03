"""Модуль содержит класс Сlient необходимый для расчета нумерологичесих показателей"""
from math import fabs


class Client:
    """Класс Client необходим для расчет показателей нумерологической матрицы"""

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

        # Расчёт дополнительных чиселл
        self.additional_numbers = {
            "Первое дополнительное число": self.additional_number_1(),
            "Второе дополнительное число": self.additional_number_2(),
            "Третье дополнительное число": self.additional_number_3(),
            "Четвертое дополнительное число": self.additional_number_4(),
        }

        # Создание строчки для расчёта основных показателей
        self.text_search = self.create_string_for_main_calculate()

        # Расчёт основных показателей
        self.general_numbers = {
            "Характер": self.text_search.count("1"),
            "Енергия": self.text_search.count("2"),
            "Интерес": self.text_search.count("3"),
            "Здоровье": self.text_search.count("4"),
            "Логика": self.text_search.count("5"),
            "Труд": self.text_search.count("6"),
            "Удача": self.text_search.count("7"),
            "Долг": self.text_search.count("8"),
            "Память": self.text_search.count("9"),
        }

        # Расчёт вторых дополнительных показателей
        self.second_general_numbers = {
            "Быт": self.text_search.count("4") + self.text_search.count("5") + self.text_search.count("6"),
            "Темперамент": self.text_search.count("3") + self.text_search.count("5") + self.text_search.count("7"),
            "Цель": self.text_search.count("1") + self.text_search.count("4") + self.text_search.count("7"),
            "Семья": self.text_search.count("2") + self.text_search.count("5") + self.text_search.count("8"),
            "Привычки": self.text_search.count("3") + self.text_search.count("6") + self.text_search.count("9"),
            "Числосудьбы": self.reduce_to_single_digit(),
        }

    def reduce_to_single_digit(self):
        value = self.additional_number_2()
        while value >= 10 and value != 11:
            value -= 9
        return value

    def additional_number_1(self):
        """Функция для расчёта первого дополнительного числа"""
        return sum(int(i) for i in self.birthday if i.isdigit())

    def additional_number_2(self):
        """Функция для расчёта второго дополнительного числа"""
        return sum(int(i) for i in str(self.additional_number_1()))


    def additional_number_3(self):
        # sourcery skip: assign-if-exp, inline-immediately-returned-variable, lift-return-into-if
        """Функция для расчёта третьего дополнительного числа"""
        if int(self.birthday[0]) != 0:
            additional_number_3 = int(
                fabs(self.additional_number_1() - (2 * int(self.birthday[0])))
            )
        else:
            additional_number_3 = int(
                fabs(self.additional_number_1() - (2 * int(self.birthday[1])))
            )
        return additional_number_3

    def additional_number_4(self):
        """Функция для расчёта четвертого дополнительного числа"""
        return sum(int(i) for i in str(self.additional_number_3()))

    def create_string_for_main_calculate(self):
        """Создание строки для вычисления основных показателей"""
        start_string = (
                self.birthday
                + str(self.additional_number_1())
                + str(self.additional_number_2())
                + str(self.additional_number_3())
                + str(self.additional_number_4())
        )
        text_search = [i for i in start_string if i.isdigit()]
        return text_search

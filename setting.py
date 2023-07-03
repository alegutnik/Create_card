from PIL import ImageFont

# Задаем настройки
MM = 3.125  # значение для перевода px -> mm
WIDTH_CELL = 125  # ширина стандартной ячейки
HEIGHT_CELL = 100  # высота стандартной ячейки
WIDTH = 592  # ширина листа ячейки
HEIGHT = 512  # высота листа ячейки
FONT_SIZE = 18 * MM  # размер шрифта

# Задаем цвет в формате HEX
TEXT_COLOR_BLUE = (9, 26, 76)  # Синий
TEXT_COLOR_WHITE = (255, 255, 255)  # Белый

# Загружаем шрифт
font_path = './font/Klein-Medium.ttf'
font = ImageFont.truetype(font_path, FONT_SIZE)


# Создаем функцию для выбора background
def get_background(language, gender):
    templates = {
        ("RUS", "Woman"): "./template/Шаблон RUS.png",
        ("UKR", "Woman"): "./template/Шаблон UKR.png",
        ("RUS", "Man"): "./template/Шаблон UKR man.png",
        ("UKR", "Man"): "./template/Шаблон UKR man.png"
    }

    key = (language, gender)
    if key in templates:
        return templates[key]
    print("Шаблон не найден!!!")
    return None


# Функция для вычисления координаты вставки
def coordinates(rows, columns):
    x = WIDTH_CELL / 2 + (WIDTH_CELL + 3) * (rows - 1)
    if rows > 3:
        x += 25
    y = (HEIGHT_CELL + 3) * (columns - 1) + 60
    return x, y


# Координаты дополнительных показательей
coordinats_second_numbers = dict(Быт=coordinates(2, 5), Темперамент=coordinates(4, 1), Цель=coordinates(4, 2),
                                 Семья=coordinates(4, 3), Привычки=coordinates(4, 4), Числосудьбы=coordinates(3, 1))

# Координаты основных чисел
coordinats_general_numbers = dict(Характер=coordinates(1, 2), Енергия=coordinates(1, 3), Интерес=coordinates(1, 4),
                                  Здоровье=coordinates(2, 2), Логика=coordinates(2, 3), Труд=coordinates(2, 4),
                                  Удача=coordinates(3, 2), Долг=coordinates(3, 3), Память=coordinates(3, 4))


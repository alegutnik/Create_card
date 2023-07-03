from PIL import Image, ImageDraw
import os

from client import Client
from setting import *


class Card:
    def __init__(self, name, birthday, language, gender):
        self.name = name
        self.birthday = birthday
        self.language = language
        self.gender = gender

        # Создаем клиента
        client = Client(self.name, self.birthday)

        # Функция для вставки значений словаря по координатам
        def insert_numbers(coordinate, client_numbers, font_color, general=True):
            for count, (key, value) in enumerate(coordinate.items(), start=1):
                if general:
                    text = str(count) * client_numbers.get(key) if client.general_numbers.get(key) != 0 else "-"
                else:
                    text = str(client.second_general_numbers.get(key)) if client.second_general_numbers.get(
                        key) != 0 else "-"
                temp = ImageFont.truetype(font_path, FONT_SIZE)
                text_box = draw.textbbox((0, 0), text, font=temp)
                text_width = text_box[2] - text_box[0]
                text_height = text_box[3] - text_box[1]
                text_x = coordinate.get(key)[0] * MM - text_width // 2
                text_y = coordinate.get(key)[1] * MM - text_height // 2 - 4 * MM
                draw.text(xy=(text_x, text_y), text=text, font=temp, fill=font_color)

        # Функция для вставки значений по координатам
        def insert_value(coordinate, text, font_color):
            temp = ImageFont.truetype(font_path, FONT_SIZE)
            text_box = draw.textbbox((0, 0), text, font=temp)
            text_width = text_box[2] - text_box[0]
            text_height = text_box[3] - text_box[1]
            text_x = coordinate[0] * MM - text_width // 2
            text_y = coordinate[1] * MM - text_height // 2 - 4 * MM
            draw.text(xy=(text_x, text_y), text=text, font=temp, fill=font_color)

        # Открываем основное изображение
        background = Image.open(get_background(self.language, self.gender))

        # Создаем новое изображение с размерами основного изображения
        new_image = Image.new("RGBA", background.size)  # Используем "RGBA" для поддержки прозрачности

        # Создаем объект ImageDraw для рисования на изображении
        draw = ImageDraw.Draw(new_image)

        # Вставляем главные показатели
        insert_numbers(coordinate=coordinats_general_numbers,
                       client_numbers=client.general_numbers,
                       font_color=TEXT_COLOR_BLUE)

        # Вставляем дополнительные показатели
        insert_numbers(coordinate=coordinats_second_numbers,
                       client_numbers=client.second_general_numbers,
                       font_color=TEXT_COLOR_WHITE,
                       general=False)

        # Вставляем имя
        insert_value(coordinate=(WIDTH_CELL, 30),
                     text=name,
                     font_color=TEXT_COLOR_WHITE)
        # Вставляем день рождения
        insert_value(coordinate=(WIDTH_CELL, 60),
                     text=birthday,
                     font_color=TEXT_COLOR_WHITE)

        # Комбинируем фоновое изображение и текстовый слой
        result = Image.alpha_composite(background.convert("RGBA"), new_image)

        # Создаем папку, если она не существует
        folder_path = "result"
        os.makedirs(folder_path, exist_ok=True)

        # Сохраняем новое изображение в файл
        result.save(f"result/{self.name}_{self.birthday}.png", "PNG")
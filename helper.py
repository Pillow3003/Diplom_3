import random
import string


class RandomUserData:
    """
    Класс для генерации случайных данных пользователя:
    имени, email и пароля.
    """

    @staticmethod
    def random_string(length: int) -> str:
        """
        Генерирует случайную строку заданной длины,
        состоящую из строчных букв, цифр и символов "_.-".

        :param length: длина генерируемой строки
        :return: сгенерированная строка
        """
        special_symbols = "_.-"
        string_symbols = string.ascii_lowercase + string.digits + special_symbols
        return ''.join(random.choices(string_symbols, k=length))

    def user_data_generation(self) -> dict:
        """
        Генерирует словарь с рандомными данными пользователя.

        :return: dict с ключами 'name', 'email', 'password'
        """
        user_data = {
            'name': self.random_string(6),
            'email': self.random_string(8) + '@gmail.com',
            'password': self.random_string(6)
        }
        return user_data
import doctest

class Pot:
    def __init__(self, volume_pot: float, volume_water: float):
    """
    Создание и подготовка к работе объекта "Кастрюля"

    :param volume_pot: Объем кострюли
    :param volume_water: Объем воды в кострюле

    Примеры:
    >>> pot = Glass(1000, 200)  # инициализация экземпляра класса
    """

    if not isinstance(volume_pot, (int, float)):
        raise TypeError("Объем кострюли должен быть типа int или float")
    if volume_pot <= 0:
        raise ValueError("Объем кострюли должен быть положительным числом")
    self.volume_pot = volume_pot

    if not isinstance(volume_water, (int, float)):
        raise TypeError("Количество воды должно быть int или float")
    if volume_water < 0:
        raise ValueError("Количество воды не может быть отрицательным числом")
        self.volume_water = volume_water

        def is_empty_pot(self) -> bool:
        """
        Функция которая проверяет является ли кострюля пустой
        :return: Является ли кострюля пустой
        Примеры:
        >>> pot = Pot(1000, 200)
        >>> pot.is_empty_pot()
        """
        ...

        def add_water_to_pot(self, water: float) -> None:
        """
        Добавление воды в кострюлю.
        :param water: Объем добавляемой воды
        :raise ValueError: Если количество добавляемой воды превышает свободное место в кострюле, то вызываем ошибку
        Примеры:
        >>> pot = Pot(1000, 200)
        >>> pot.add_water_to_pot(600)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая вода должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая вода должна положительным числом")
        ...

        def remove_water_from_pot(self, estimate_water: float) -> None:
            """
            Извлечение воды из кострюли.
            :param estimate_water: Объем извлекаемой воды
            :raise ValueError: Если количество извлекаемой воды превышает количество воды в кострюле,
            то возвращается ошибка.
            :return: Объем реально извлеченной воды
            Примеры:
            >>> pot = Pot(1000, 800)
            >>> pot.remove_water_from_pot(600)
            """
            ...
class Telegram_chanel:
    def __init__(self, followers: int, max_followers: int):
    """
    Создание и подготовка к работе объекта "Телеграм канал"

    :param followers: Количество полдписчиков
    :param max_followers: Максимальное количество подписчиков

    Примеры:
    >>> Telegram_chanel = Telegram_chanel(10000, 0)  # инициализация экземпляра класса
    """

    if not isinstance(followers, (int, float)):
        raise TypeError("Количество подписчиков должно быть типа int или float")
    if followers <= 0:
        raise ValueError("Количество подписчиков должно быть положительным числом")
    self.followers = followers

    if not isinstance(max_follower, (int, float)):
        raise TypeError("Максимальное количество подписчиков должно быть типа int или float")
    if max_follower < 0:
        raise ValueError("Максимальное количество подписчиков не может быть отрицательным числом")
        self.max_follower = max_follower

        def is_empty_Telegram_channel(self) -> bool:
        """
        Функция которая проверяет есть ли подписчики
        :return: Есть ли подписчики
        Примеры:
        >>> telegram_channel = Telegram_channel(10000, 0)
        >>> telegram_channel.is_empty_telegram_chanel()
        """
        ...

        def add_people_to_telegram_channel(self, people: int) -> None:
        """
        Добавление людей в телеграм канал.
        :param people: количество людей
        :raise ValueError: Если количество людей превышает допустимое количество подписчиков, то вызываем ошибку
        Примеры:
        >>> telegram_channel = Telegram_channel(10000, 0)
        >>> telegram_channel.add_people_to_telegram_channel(600)
        """
        if not isinstance(people, (int, float)):
            raise TypeError("Люди должны быть типа int или float")
        if people < 0:
            raise ValueError("Количество людей должно быть положительным числом")
        ...

        def remove_people_from_telegra,_channel(self, estimate_people: float) -> None:
            """
            Удаление людей из телеграм канала.
            :param estimate_people: Количество удаленных людей
            :raise ValueError: Если количество удаленных людей превышает количество людей в телеграм канале,
            то возвращается ошибка.
            :return: Количество реально удаленных людей
            Примеры:
            >>> telegram_channel = Telegram_channel(10000, 600)
            >>> telegram_channel.remove_people_from_telegram_channel(600)
            """
            ...
class Boat:
    def __init__(self, passengers: int, max_passengers: int):
    """
    Создание и подготовка к работе объекта "Корабль"

    :param passengers: Количество пассажиров
    :param max_passengers: Максимальное количество пассажиров

    Примеры:
    >>> boat = Boat(100, 0)  # инициализация экземпляра класса
    """

    if not isinstance(passengers, (int, float)):
        raise TypeError("Количество пассажиров должно быть типа int или float")
    if passengers <= 0:
        raise ValueError("Количество пассажиров должно быть положительным числом")
    self.passengers = passengers

    if not isinstance(max_passengers, (int, float)):
        raise TypeError("Максимальное количество пассажиров должно быть int или float")
    if max_passengers < 0:
        raise ValueError("Максимальное количество пассажиров не может быть отрицательным числом")
        self.max_passengers = max_passengers

        def is_empty_boat(self) -> bool:
        """
        Функция которая проверяет есть ли пассажиры на корабле
        :return: Есть ли пассажиры на корабле
        Примеры:
        >>> boat = Boat(100, 0)
        >>> boat.is_empty_boat()
        """
        ...

        def new_passengers_to_boat(self, people: float) -> None:
        """
        На пристане заходят новые пассажиры.
        :param people: Количество новых пассажиров
        :raise ValueError: Если количество новых пассажиров превышает свободное место на корабле, то вызываем ошибку
        Примеры:
        >>> boat = Boat(100, 80)
        >>> boat.add_people_to_boat(80)
        """
        if not isinstance(people, (int, float)):
            raise TypeError("Новые пассажеры должны быть типа int или float")
        if people < 0:
            raise ValueError("Новые пассажеры должны положительным числом")
        ...

        def remove_people_from_voat(self, estimate_people: float) -> None:
            """
            Не пускать пассажиров на борт, если их больше, чем мест.
            :param estimate_people: Количество людей, которых не пустят
            :raise ValueError: Если количество людей, которых не пускают превышает количество людей на корабле,
            то возвращается ошибка.
            :return: Количество людей, которых не пускают
            Примеры:
            >>> boat = Boat(100, 80)
            >>> boat.remove_people_from_boat(80)
            """
if __name__ == "__main__":
    doctest.testmod()
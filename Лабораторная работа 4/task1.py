class Book:
    def __init__(self, name: str, length: int):
        """
        :param name: название книги
        :param length: сколько страниц в книге
       """
        self.name = name
        self.length = length

    @property
    def name(self) -> str:
        return self._name

    @property
    def length(self) -> int:
        return self.length

    def __str__(self):
        return f"Книга: {self.name} \nКоличество страниц: {self.length} стр"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, length={self.length!r}) "

class audioBook(Book):
    def __int__(self,  name: str, len: int):
        """
        :param name: название книги
        :param len: длительность книги (мин)
        """

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название книги.
        :param name: название книги
        :raise TypeError: вызов ошибки если введены данные неверного типа
        """
        if not isinstance(name, str):
            raise TypeError(f'Параметр "name" должен быть типа str')
        self._name = name

    @property
    def len(self) -> int:
        return self.len

    @len.setter
    def len(self, name: str) -> None:
        """
        Устанавливает название книги.
        :param name: название книги
        :raise ValueError: вызов ошибки если введены данные неверного типа
        """
        if not isinstance(len, int):
            raise ValueError(f'Длительность должна быть > 0')
        self._len = len


    def __str__(self):
        return f"Книга: {self.name} \nДлительность: {self.len} мин"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, len={self.len!r})"
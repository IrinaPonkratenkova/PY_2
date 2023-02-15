class Animal:
    def __init__(self, name: str, type: str):
        """
        :param name: название животного
        :param type: тип животного
       """
        self.name = name
        self.length = type

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self.type

    def __str__(self):
        return f"Животное: {self.name} \nТип животного: {self.type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, type={self.type!r}) "

class Mammals(Animal):
    def __int__(self,  name: str, order: str):
        """
        :param name: название млекопитающего
        :param order: отряд
        """

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название млекопитающего.
        :param name: название млекопитающего
        :raise TypeError: вызов ошибки если введены данные неверного типа
        """
        if not isinstance(name, str):
            raise TypeError(f'Параметр "name" должен быть типа str')
        self._name = name

    @property
    def order(self) -> int:
        return self.order

    @order.setter
    def order(self, order: str) -> None:
        """
        Устанавливает отряд.
        :param order: отряд животного
        :raise TypeError: вызов ошибки если введен не отряд животного, а род/вид..
        """
        if not isinstance(order, int):
            raise TypeError(f'Должен быть написан отряд животного')
        self._order = order


    def __str__(self):
        return f"Млекопитающие: {self.name} \nОтряд: {self.order}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, order={self.order!r})"
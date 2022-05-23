from abc import abstractmethod

from labs.models.continent import Continent
from labs.models.size import Size


class Animal:

    def __init__(self, name: str, size: Size, is_predator: bool, continent: Continent) -> None:
        self.__name = name
        self.__size = size
        self.__is_predator = is_predator
        self.__continent = continent

    def __str__(self) -> str:
        return f"My name: {self.__name} and I live in {self.__continent.value}, also I am a {self.__class__.__name__}. "

    @abstractmethod
    def do_voice(self) -> None:
        pass

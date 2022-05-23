from abc import abstractmethod

from labs.models.size import Size


class Animal:

    def __init__(self, name: str, size: Size, is_predator: bool) -> None:
        self.__name = name
        self.__size = size
        self.is_predator = is_predator

    def __str__(self) -> str:
        return f"My name: {self.__name} and i am {self.__size.value}-sized, also I am a {self.__class__.__name__}. "

    @abstractmethod
    def do_voice(self) -> None:
        pass

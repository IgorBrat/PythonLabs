from abc import abstractmethod, ABC

from labs.models.continent import Continent
from labs.models.size import Size


class Animal(ABC):
    """
    Super class
    """

    def __init__(self, name: str, size: Size, is_predator: bool, continent: Continent) -> None:
        self._name = name
        self._size = size
        self._is_predator = is_predator
        self._continent = continent

    def __repr__(self) -> str:
        return f"My name: {self._name} and I live mainly in {self._continent.value}, also I am a {self.__class__.__name__}. "

    @abstractmethod
    def do_voice(self) -> None:
        """
        Animal does some voice
        :return: None
        """

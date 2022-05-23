from labs.models.animal import Animal
from labs.models.size import Size


class Mammal(Animal):

    def __init__(self, name: str, size: Size, is_predator: bool, has_fur: bool, is_living_underwater: bool,
                 is_living_in_a_pride: bool, is_domestic: bool):
        super().__init__(name, size, is_predator)
        self.__has_fur = has_fur
        self.__is_living_underwater = is_living_underwater
        self.__is_living_in_a_pride = is_living_in_a_pride
        self.__is_domestic = is_domestic

    def __str__(self) -> str:
        return super().__str__() + f"That`s why I feed my kids with milk."

    # overriding abstract method
    def do_voice(self) -> None:
        print("Some loud mammal voices")

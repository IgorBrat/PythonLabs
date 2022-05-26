from labs.models.animal import Animal
from labs.models.continent import Continent
from labs.models.size import Size


class Insect(Animal):

    def __init__(self, name: str, size: Size, is_predator: bool, continent: Continent, count_of_legs: int,
                 has_wings: bool):
        super().__init__(name, size, is_predator, continent)
        self.__count_of_legs = count_of_legs
        self.__has_wings = has_wings

    def __str__(self) -> str:
        return super().__str__() + f"I bother people`s lives by buzzing."

    # overriding abstract method
    def do_voice(self) -> None:
        print("Buzzzzzzzing")

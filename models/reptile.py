from labs.models.animal import Animal
from labs.models.continent import Continent
from labs.models.size import Size


class Reptile(Animal):

    def __init__(self, name: str, size: Size, is_predator: bool, continent: Continent, changes_skin: bool,
                 is_poisonous: bool):
        super().__init__(name, size, is_predator, continent)
        self.__is_poisonous = is_poisonous
        self.__changes_skin = changes_skin

    def __repr__(self) -> str:
        return super().__repr__() + f"I spend some time underwater."

    # overriding abstract method
    def do_voice(self) -> None:
        print("Squeaky sounds")

from labs.models.animal import Animal
from labs.models.continent import Continent
from labs.models.size import Size


class Fish(Animal):

    def __init__(self, name: str, size: Size, is_predator: bool, continent: Continent, is_poisonous: bool,
                 lives_in_fresh_water: bool):
        super().__init__(name, size, is_predator, continent)
        self.__lives_in_fresh_water = lives_in_fresh_water
        self.__is_poisonous = is_poisonous

    def __repr__(self) -> str:
        return super().__repr__() + f"My meat is really tasty."

    # overriding abstract method
    def do_voice(self) -> None:
        print("There is no sounds underwater.")

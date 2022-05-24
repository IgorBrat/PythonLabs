from labs.models.animal import Animal
from labs.models.continent import Continent
from labs.models.size import Size


class Bird(Animal):

    def __init__(self, name: str, size: Size, is_predator: bool, continent: Continent, can_fly: bool, is_domestic: bool,
                 has_teeth: bool, has_feathers: bool):
        super().__init__(name, size, is_predator, continent)
        self.__has_feathers = has_feathers
        self.__has_teeth = has_teeth
        self.__can_fly = can_fly
        self.__is_domestic = is_domestic

    def __repr__(self) -> str:
        return super().__repr__() + f"So, as you know, I lay eggs."

    # overriding abstract method
    def do_voice(self) -> None:
        print("Some bird squawking")

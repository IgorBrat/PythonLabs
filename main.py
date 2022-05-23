from labs.models.animal import Animal
from labs.models.bird import Bird
from labs.models.continent import Continent
from labs.models.mammal import Mammal
from labs.models.size import Size


def main() -> None:
    dog = Mammal("Doggo Barney", Size.MEDIUM, True, Continent.EURASIA, has_fur=True, is_living_underwater=False,
                 is_living_in_a_pride=False,
                 is_domestic=True)
    bird = Bird("James the Penguin", Size.MEDIUM, True, Continent.ANTARCTICA, can_fly=False, has_teeth=True,
                has_feathers=True, is_domestic=False)
    dog.do_voice()
    print(dog.__str__())
    bird.do_voice()
    print(bird.__str__())


if __name__ == "__main__":
    main()

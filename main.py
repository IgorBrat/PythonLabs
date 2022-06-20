from labs.models.bird import Bird
from labs.models.continent import Continent
from labs.models.fish import Fish
from labs.models.insect import Insect
from labs.models.mammal import Mammal
from labs.models.reptile import Reptile
from labs.models.size import Size


def main() -> None:
    dog = Mammal("Doggo Barney", Size.MEDIUM, True, Continent.EURASIA, has_fur=True, is_living_underwater=False,
                 is_living_in_a_pride=False,
                 is_domestic=True)
    bird = Bird("James the Penguin", Size.MEDIUM, True, Continent.ANTARCTICA, can_fly=False, has_teeth=True,
                has_feathers=True, is_domestic=False)
    insect = Insect("Lil Buzzy", Size.SMALL, False, Continent.EURASIA, has_wings=True, count_of_legs=6)
    reptile = Reptile("Goward Gecko", Size.SMALL, True, Continent.SOUTH_AMERICA, changes_skin=True, is_poisonous=False)
    fish = Fish("Gordo Crucian", Size.SMALL, False, Continent.EURASIA, is_poisonous=False, lives_in_fresh_water=True)
    dog.do_voice()
    print(dog.__str__())
    bird.do_voice()
    print(bird.__str__())
    insect.do_voice()
    print(insect.__str__())
    reptile.do_voice()
    print(reptile.__str__())
    fish.do_voice()
    print(fish.__str__())


if __name__ == "__main__":
    main()

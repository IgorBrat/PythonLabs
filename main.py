from labs.models.animal import Animal
from labs.models.mammal import Mammal
from labs.models.size import Size


def main() -> None:
    dog = Mammal("Doggo Barney", Size.MEDIUM, True, has_fur=True, is_living_underwater=False, is_living_in_a_pride=False,
                 is_domestic=True)
    dog.do_voice()
    print(dog.__str__())


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod



class Character(ABC):
    def __init__(self, name, health, attack_power, x, y):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.x = x
        self.y = y

    @abstractmethod
    def display_info(self):
        pass



class Warrior(Character):
    def __init__(self, x, y):
        super().__init__("Warrior", health=150, attack_power=20, x=x, y=y)

    def display_info(self):
        print(f"{self.name} [Health: {self.health}, Attack: {self.attack_power}, Position: ({self.x}, {self.y})]")


class Mage(Character):
    def __init__(self, x, y):
        super().__init__("Mage", health=100, attack_power=50, x=x, y=y)

    def display_info(self):
        print(f"{self.name} [Health: {self.health}, Attack: {self.attack_power}, Position: ({self.x}, {self.y})]")


class Archer(Character):
    def __init__(self, x, y):
        super().__init__("Archer", health=120, attack_power=30, x=x, y=y)

    def display_info(self):
        print(f"{self.name} [Health: {self.health}, Attack: {self.attack_power}, Position: ({self.x}, {self.y})]")



class CharacterFactory:
    @staticmethod
    def create_character(character_type, x, y):
        if character_type == "warrior":
            return Warrior(x, y)
        elif character_type == "mage":
            return Mage(x, y)
        elif character_type == "archer":
            return Archer(x, y)
        else:
            raise ValueError("Unknown character type")



class Arena:
    def __init__(self):
        self.characters = []
        self.observers = []

    def add_character(self, character):
        self.characters.append(character)
        print(f"{character.name} has entered the Arena at position ({character.x}, {character.y}).")
        self.notify_observers(character)

    def notify_observers(self, character):
        for observer in self.observers:
            observer.update(character)

    def add_observer(self, observer):
        self.observers.append(observer)

    def show_characters(self):
        print("\nCurrent Characters in Arena:")
        for character in self.characters:
            character.display_info()



class Observer:
    def update(self, character):
        print(f"Observer: New character added - {character.name} at position ({character.x}, {character.y}).")



if __name__ == "__main__":

    arena = Arena()


    observer = Observer()
    arena.add_observer(observer)


    factory = CharacterFactory()
    character1 = factory.create_character("warrior", 0, 0)
    character2 = factory.create_character("mage", 5, 5)
    character3 = factory.create_character("archer", 3, 4)


    arena.add_character(character1)
    arena.add_character(character2)
    arena.add_character(character3)


    arena.show_characters()

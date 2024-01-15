from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack_power(self):
        pass
class Armor(ABC):
    @abstractmethod
    def up_health(self):
        pass
class Warrior(ABC):
    @abstractmethod
    def beat(self):
        pass
    @abstractmethod
    def protection(self):
        pass

class NegativeDamage(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message=message
        self.value = value
        if self.value <= 0:
            raise self
    def __str__(self):
        return self.message

class NegativeHealth(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message=message
        self.value = value
        if self.value <= 0:
            raise self
    def __str__(self):
        return self.message

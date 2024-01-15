from abc import ABC, abstractmethod
class Technic(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Hoover(Technic):
    def turn_on(self):
        return super.turn_on()
    def turn_off(self):
        return super.turn_of()
class Multicooker(Technic):
    def turn_on(self):
        return super.turn_on()
    def turn_off(self):
        return super.turn_of()
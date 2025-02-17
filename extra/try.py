from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        print("AbstractClassExample: Initial step")

    @abstractmethod
    def do_another_thing(self):
        print("AbstractClassExample: Another initial step")

class ConcreteClassExample(AbstractClassExample):
    def do_something(self):
        print("ConcreteClassExample: Doing something more!")  # Doesn't call the base class's print

    def do_another_thing(self):
        super().do_another_thing() #call the abstarct method and prints its statement
        print("ConcreteClassExample: Doing another thing!")

concrete_instance = ConcreteClassExample()
concrete_instance.do_something() # Output: ConcreteClassExample: Doing something more! (base class print is skipped)
concrete_instance.do_another_thing()

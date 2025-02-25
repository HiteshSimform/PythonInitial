class BaseClass:
    def __init__(self):
        # Private constructor logic
        self._value = "This is a value from the BaseClass"

    @classmethod
    def create_instance(cls):
        # Public method to create an instance
        return cls()

class DerivedClass(BaseClass):
    def __init__(self):
        # Call the private constructor of BaseClass
        super().__init__()
        self._derived_value = "This is a value from the DerivedClass"

    def display_values(self):
        print(self._value)
        print(self._derived_value)

# Usage
# Creating an instance of DerivedClass using the public method of BaseClass
derived_instance = DerivedClass.create_instance()
derived_instance.display_values()

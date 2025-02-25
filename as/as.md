Certainly! Let's refactor the program into a class-based structure. This will encapsulate the functionality into a more organized and object-oriented manner. I'll use class methods, static methods, and instance methods where appropriate.

The primary classes will be:

1. `NumberConverter`: To handle the word-to-number and number-to-word conversions.
2. `MathOperations`: To handle the GCD calculation.
3. `MainProgram`: To integrate the user interaction with the functionality.

### 1. **NumberConverter Class**:
We'll keep the conversion functions (`word_to_num` and `num_to_word`) inside a class to logically group them together. The functions can be `staticmethods` because they don’t need access to instance variables.

### 2. **MathOperations Class**:
The `gcd` method will be part of this class as a `staticmethod`.

### 3. **MainProgram Class**:
This will be the entry point where user interaction takes place.

### Here's the class-based structure:

```python
# number_utils.py

class NumberConverter:
    # Dictionary mapping digits to their word form
    digits = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    @staticmethod
    def word_to_num(string: str) -> str:
        """
        Converts a word representing a number to its numerical value.

        Args:
            string (str): A string representing a number in word form.

        Returns:
            str: The numerical value of the input string as a string.

        Raises:
            ValueError: If Input String does not start with a valid word.
        """
        if not string:
            return ""
        
        if string.startswith('zero'):
            return '0' + NumberConverter.word_to_num(string[4:])
        elif string.startswith('one'):
            return '1' + NumberConverter.word_to_num(string[3:])
        elif string.startswith('two'):
            return '2' + NumberConverter.word_to_num(string[3:])
        elif string.startswith('three'):
            return '3' + NumberConverter.word_to_num(string[5:])
        elif string.startswith('four'):
            return '4' + NumberConverter.word_to_num(string[4:])
        elif string.startswith('five'):
            return '5' + NumberConverter.word_to_num(string[4:])
        elif string.startswith('six'):
            return '6' + NumberConverter.word_to_num(string[3:])
        elif string.startswith('seven'):
            return '7' + NumberConverter.word_to_num(string[5:])
        elif string.startswith('eight'):
            return '8' + NumberConverter.word_to_num(string[5:])
        elif string.startswith('nine'):
            return '9' + NumberConverter.word_to_num(string[4:])
        
        raise ValueError("Invalid input: does not start with a valid number in words.")

    @staticmethod
    def num_to_word(num: str) -> str:
        """
        Converts a number to a word representing that number.

        Args:
            num (str): A string representing a number.

        Returns:
            str: A string representing the input number in word form.
        """
        if num == '':
            return ''
        
        return NumberConverter.digits[num[0]] + NumberConverter.num_to_word(num[1:])


# math_utils.py

class MathOperations:
    @staticmethod
    def gcd(number1: int, number2: int) -> int:
        """
        Computes the GCD of two numbers using recursion.

        Args:
            number1 (int): The first integer.
            number2 (int): The second integer.

        Returns:
            int: The GCD of the input integers.
        
        Raises:
            TypeError: If inputs are not integers.
        """
        
        if number2 == 0:
            return number1
        else:
            return MathOperations.gcd(number2, number1 % number2)


# main.py

from number_utils import NumberConverter
from math_utils import MathOperations

class MainProgram:
    @staticmethod
    def run():
        try:
            # Prompt the user to enter the Input in word form
            inputstr1 = input("Please enter input 1: ").lower()
            inputnum1 = int(NumberConverter.word_to_num(inputstr1))

            inputstr2 = input("Please enter input 2: ").lower()
            inputnum2 = int(NumberConverter.word_to_num(inputstr2))

            gcd_num = str(MathOperations.gcd(inputnum1, inputnum2))

            print(f"GCD of {inputstr1} and {inputstr2} is {NumberConverter.num_to_word(gcd_num)}")

        except ValueError as ve:
            print(ve)

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    MainProgram.run()
```

### Breakdown:

1. **`NumberConverter` Class**:
    - Contains `word_to_num` and `num_to_word` as `staticmethods`, since these methods don't need an instance to operate. They perform the word-to-number and number-to-word conversions.
  
2. **`MathOperations` Class**:
    - Contains the `gcd` function as a `staticmethod`. The GCD function is a utility function that doesn't require an instance of the class to work, making it static.

3. **`MainProgram` Class**:
    - The `MainProgram` class has a single `run()` static method that handles user input and prints the result. It's the main driver of the application.

4. **Reduced Time Complexity**:
    - The time complexity of converting a word to a number and vice versa is dependent on the length of the string. This is optimal given the constraints.
    - The GCD computation remains `O(log(min(a, b)))`, which is already efficient.

### Directory Structure:

```
your_project/
│
├── main.py           # Main program entry point
├── number_utils.py   # Contains NumberConverter class
└── math_utils.py     # Contains MathOperations class
```

### How to Run:

1. Save the code in the respective files (`number_utils.py`, `math_utils.py`, `main.py`).
2. Run the program from the terminal:

```bash
python main.py
```

### Advantages of this Structure:

1. **Encapsulation**: The functionality is encapsulated within appropriate classes (`NumberConverter` for conversions, `MathOperations` for GCD calculations).
2. **Extendability**: New mathematical or conversion functions can be added easily by adding new static methods to their respective classes.
3. **Separation of Concerns**: Each class has a clear responsibility, improving maintainability.
4. **Minimal Complexity**: The time complexity remains the same, but the code is more structured and easier to maintain.
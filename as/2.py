class ParenthesesGenerator:
    def __init__(self, n):
        self.n = n  # The number of pairs of parentheses
        self.result = []

    def generateParentheses(self):
        # Start the backtracking process
        self._backtrack('', 0, 0)
        return self.result

    def _backtrack(self, current_str, open_count, close_count):
        # If the current string is valid, and we've used all parentheses, add to result
        if len(current_str) == 2 * self.n:
            self.result.append(current_str)
            return
        
        # Add an open parenthesis if we haven't used all of them yet
        if open_count < self.n:
            self._backtrack(current_str + '(', open_count + 1, close_count)
        
        # Add a close parenthesis if we have more open parentheses than close
        if close_count < open_count:
            self._backtrack(current_str + ')', open_count, close_count + 1)


class ParenthesesHandler:
    def __init__(self, n):
        self.generator = ParenthesesGenerator(n)

    def getCombinations(self):
        # Return the list of generated well-formed parentheses combinations
        return self.generator.generateParentheses()


# Example Usage
def generate_all_parentheses(n):
    handler = ParenthesesHandler(n)
    return handler.getCombinations()


# Test with n = 3
n = 3
result = generate_all_parentheses(n)
print(f"Generated Parentheses for n={n}: {result}")

# Test with n = 1
n = 1
result = generate_all_parentheses(n)
print(f"Generated Parentheses for n={n}: {result}")

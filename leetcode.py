class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generates the kth lexicographically happy string of length n (optimized backtracking).
        """
        print(f"Debugging: n={n}, k={k}")  # Initial debugging

        total_happy_strings = 3 * (2**(n - 1))
        print(f"Debugging: total_happy_strings={total_happy_strings}")
        if k > total_happy_strings:
            print("Debugging: k is out of range")
            return ""

        result = ""
        options = ['a', 'b', 'c']

        for i in range(n):
            print(f"Debugging: Loop iteration i={i}")
            half = (2**(n - i - 1))
            print(f"Debugging: half={half}")

            valid_chars = []
            for char in options:
                if not result or char != result[-1]:
                    valid_chars.append(char)
            print(f"Debugging: valid_chars={valid_chars}")

            found_char = False  # Flag to check if a char was added in this iteration
            for char in valid_chars:
                print(f"Debugging: Trying char={char}")
                if k <= half:
                    result += char
                    options = ['a', 'b', 'c']  # Reset options. Not strictly necessary, but keeps code cleaner.
                    print(f"Debugging: Appended char={char}, result={result}, k={k}")
                    found_char = True
                    break
                else:
                    k -= half
                    print(f"Debugging: Skipping char={char}, k is now={k}")

            if not found_char:
                print("Debugging: No valid character found in this iteration.  This should not happen.")
                return ""  # indicates error. This *shouldn't* happen with the given logic.

        print(f"Debugging: Final result={result}")
        return result

# Test Cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    n1 = 3
    k1 = 5
    result1 = solution.getHappyString(n1, k1)
    print(f"Test Case 1: n={n1}, k={k1}, Result: {result1}")  # Expected: "acb"

    # Test case 2
    n2 = 1
    k2 = 3
    result2 = solution.getHappyString(n2, k2)
    print(f"Test Case 2: n={n2}, k={k2}, Result: {result2}")  # Expected: "c"

    # Test case 3
    n3 = 1
    k3 = 4
    result3 = solution.getHappyString(n3, k3)
    print(f"Test Case 3: n={n3}, k={k3}, Result: {result3}")  # Expected: ""

    # Test case 4
    n4 = 2
    k4 = 7
    result4 = solution.getHappyString(n4, k4)
    print(f"Test Case 4: n={n4}, k={k4}, Result: {result4}")  # Expected: ""

    # Test case 5
    n5 = 3
    k5 = 9
    result5 = solution.getHappyString(n5, k5)
    print(f"Test Case 5: n={n5}, k={k5}, Result: {result5}") # Expected: cab

    # Test case 6
    n6 = 10
    k6 = 100
    result6 = solution.getHappyString(n6, k6)
    print(f"Test Case 6: n={n6}, k={k6}, Result: {result6}")

    # Test case 7: Edge case - k=1
    n7 = 3
    k7 = 1
    result7 = solution.getHappyString(n7, k7)
    print(f"Test Case 7: n={n7}, k={k7}, Result: {result7}")  # Expected: "aba"

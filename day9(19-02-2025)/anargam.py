from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups a list of strings into sublists, where each sublist contains anagrams of each other.

    Args:
        strs: A list of strings.

    Returns:
        A list of lists, where each inner list contains strings that are anagrams of each other.
    """

    d = defaultdict(list)  # Use defaultdict for easy grouping

    print(f"Initial defaultdict: {d}")  # Debug: Inspect the initial state

    for s in strs:
        print(f"Processing string: {s}")  # Debug: Track the current string

        # Input validation: Check if the element is a string
        if not isinstance(s, str):
            print(f"Error: Input element {s} is not a string. Skipping.") #Debug:Error message
            continue

        k = "".join(sorted(s))  # Create a sorted string as the key

        print(f"Sorted string (key): {k}")  # Debug: Inspect the generated key

        d[k].append(s)  # Add the string to the corresponding list in the defaultdict

        print(f"Current defaultdict state: {d}")  # Debug: See how the defaultdict is updated

    result = list(d.values())  # Convert the values of the defaultdict to a list of lists

    print(f"Final result: {result}")  # Debug: Inspect the final result before returning

    return result

# Example usage and testing:
if __name__ == '__main__':
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["", ""],
        ["listen", "silent", "hello", "world", "dlorw"],
        ["Eat", "tea", "tan", "ate", "nat", "bat"], #Example with mixed casing to check case sensitivity
        [123, "tea", "tan", "ate", "nat", "bat"]  #Example with non-string element to check error handling
    ]

    for strs in test_cases:
        print(f"\nInput: {strs}")
        grouped_anagrams = groupAnagrams(strs)
        print(f"Output: {grouped_anagrams}") #Print the output for each test case

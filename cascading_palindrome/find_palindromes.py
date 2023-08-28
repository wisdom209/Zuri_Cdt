"""Module that finds palindromes within a given string"""


class Palindromes:
    """A class that finds the palindromes in a string"""

    def __init__(self, *args, **kwargs):
        """Initialize the class with no arguments"""

    def __is_palindrome(self, check_str):
        """returns true if a string is a palindrome otherwise false"""
        left = 0
        right = len(check_str) - 1

        if right <= 0:
            # single letters and empty strings are not palindromes
            return False

        while left < right:
            if check_str[left] != check_str[right]:
                # Reduces iterations to at most half the string size
                return False
            left += 1
            right -= 1
        return True

    def find_palindromes_in_str(self, inputString=None):
        """Checks for the palindromes in the given string"""
        if type(inputString) is not str:
            return "Error: find_palindromes_in_str() takes a string argument"

        strings_to_check = inputString.split()
        str_with_palindromes = ""

        for index, str_to_check in enumerate(strings_to_check):
            # add str_to_check to str_with_palindromes if a palindrome
            if self.__is_palindrome(str_to_check):
                if index == 0:
                    str_with_palindromes += str_to_check
                else:
                    str_with_palindromes += f" {str_to_check}"

        if not str_with_palindromes:
            # str_with_palindromes will be empty if no palindromes are found
            return f"No palindromes in the given string: {inputString}"

        return str_with_palindromes


if __name__ == '__main__':
    """Test out the algorithm"""
    palindrome_finder = Palindromes()

    # Example 1
    palindromes = palindrome_finder.find_palindromes_in_str("1230321")
    print(palindromes)

    # Example 2
    palindromes = palindrome_finder.find_palindromes_in_str(
        "1230321 09234 0124210")
    print(palindromes)

    # Example 3
    palindromes = palindrome_finder.find_palindromes_in_str(
        "abcd5dcba 1230321 09234 0124210")
    print(palindromes)

    # Example 4
    palindromes = palindrome_finder.find_palindromes_in_str(123535436)
    print(palindromes)

    # Example 5
    palindromes = palindrome_finder.find_palindromes_in_str(
        "                racecar radar                    level")
    print(palindromes)

    # Example 6
    palindromes = palindrome_finder.find_palindromes_in_str(
        "apple b banana cherry")
    print(palindromes)

    # Example 7
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 8
    palindromes = palindrome_finder.find_palindromes_in_str(
        "1234321 56765 890098")
    print(palindromes)

    # Example 9
    palindromes = palindrome_finder.find_palindromes_in_str(" ")
    print(palindromes)

    # Example 10
    palindromes = palindrome_finder.find_palindromes_in_str("hello world")
    print(palindromes)

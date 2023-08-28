"""Module that finds palindromes within a given string"""


class Palindromes:
    """A class that finds the palindromes in a string"""

    def __init__(self, inputString=None):
        """initialize the class"""
        self.__inputString = inputString

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

    def find_palindromes_in_str(self, *args, **kwargs):
        """Checks for the palindromes in the given string"""
        if type(self.__inputString) is not str:
            return f"MESSAGE: find_palindromes_in_str() takes a string but {type(self.__inputString)} was given"
        if len(self.__inputString.strip()) == 0:
            return f"MESSAGE: An empty string has no palindromes"

        strings_to_check = self.__inputString.split()
        str_with_palindromes = ""

        for index, str_to_check in enumerate(strings_to_check):
            # append str_to_check to str_with_palindromes if a palindrome
            if self.__is_palindrome(str_to_check):
                if index == 0:
                    str_with_palindromes += str_to_check
                else:
                    str_with_palindromes += f" {str_to_check}"

        if not str_with_palindromes:
            # str_with_palindromes will be empty if no palindromes are found
            return f"No palindromes in the given string: {self.__inputString}"

        return str_with_palindromes


if __name__ == '__main__':
    """Test out the algorithm"""

    # Example 1
    palindrome_finder = Palindromes("1230321")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 2
    palindrome_finder = Palindromes("1230321 09234 0124210")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 3
    palindrome_finder = Palindromes("abcd5dcba 1230321 09234 0124210")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 4
    palindrome_finder = Palindromes(123535436)
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 5
    palindrome_finder = Palindromes("   racecar radar    level")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 6
    palindrome_finder = Palindromes("apple b banana cherry")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 7
    palindrome_finder = Palindromes()
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 8
    palindrome_finder = Palindromes("1234321 56765 890098")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 9
    palindrome_finder = Palindromes("")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

    # Example 10
    palindrome_finder = Palindromes("hello world")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)

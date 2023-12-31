# Cascading Palindromes

- Module creates a Palindrome class with a function(`find_palindromes_in_str()`) that finds the palindromes in a given string. 
- For example, if a string such as `'1230321 01234 0124210'` is used to initialize the class, it will return `1230321 0124210`.
- if no palindromes are found in the string such as `'apple b banana cherry'`, it will return `'No palindromes in the given string: apple b banana cherry'`
- Single letters or empty strings are not considered as palindromes.
- if no argument is used to initialize the classs or given argument is not a string it will return an error message

## Requirement
- Python 3.6 or higher

## Usage
- Examples are already provided in the find_palindromes module
- Assuming you want to test the programme in another module within the same directory 
    
	```
	from find_palindromes import Palindromes

    palindrome_finder = Palindromes("1230321")
    palindromes = palindrome_finder.find_palindromes_in_str()
    print(palindromes)
	```
- To run the examples already provided, run this command: `python3 find_palindromes.py`

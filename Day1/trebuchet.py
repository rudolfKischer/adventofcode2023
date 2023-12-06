import os
import re

puzzle_path = 'trebuchet.txt'

def extract_digits(line):
    # Dictionary to convert spelled-out numbers to digits
    number_words = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Replace spelled-out numbers with digits
    for word, digit in number_words.items():
        line = line.replace(word, digit)

    # Extract digits from the modified line
    digits = [char for char in line if char.isdigit()]

    # Return the combined first and last digit as a number, if there are enough digits
    return int(digits[0] + digits[-1]) if digits else 0


digits = {
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6, 
    "seven": 7, 
    "eight": 8, 
    "nine": 9,
}

pattern = '|'.join(map(re.escape, digits.keys()))
pattern += '|\d'
with open(puzzle_path) as puzzle_file:
    val = 0
    for line in puzzle_file:
        z = re.findall(pattern, line)
        print(line)
        print(z)
        z = [ digits.get(x, x) for x in z]
        z = list(map(int,z))
        print(z)
        num = int(f'{z[0]}{z[-1]}')
        # val += num
        val += extract_digits(line)
    print(val)


        
    



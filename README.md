# NATO Alphabet
The program takes an input word from the user and converts each letter into the corresponding NATO phonetic alphabet code. For example, if the user enters "hello", the program will output "Hotel Echo Lima Lima Oscar".

The program handles user input, converts it to uppercase, and checks whether each letter is valid in the alphabet. If an invalid character is entered (e.g., a number or symbol), the user is prompted to enter a valid word again.

## Requirements
- Python 3.x
- pandas library

## How to Use
1. Run the Game: Execute the main.py script. This will prompt you to enter a word.

2. Enter a Word: The program will take your input (case-insensitive) and convert each letter into the corresponding NATO phonetic code.

3. Invalid Input Handling: If you enter anything other than a letter (e.g., a number or special character), the program will prompt you again to enter a valid word containing only letters from the alphabet.

4. See the Results: The program will display the NATO phonetic code for the word you entered.

## How It Works
- The NATO phonetic alphabet is stored in a CSV file (nato_phonetic_alphabet.csv) with the letters and their corresponding phonetic codes.
- The program reads this CSV using pandas and stores the data in a dictionary (dic), where the keys are letters (A-Z) and the values are the corresponding phonetic codes.
- The generate() function prompts the user to input a word. It converts the word to uppercase and checks each letter against the dictionary.
- If the letter is valid (i.e., it exists in the dictionary), its phonetic code is appended to the result list. If the input contains any invalid characters (non-alphabetic), the program will ask the user to input a valid word again.

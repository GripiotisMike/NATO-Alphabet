# Importing the pandas library to handle reading the CSV file
import pandas

# Reading the CSV file into a pandas DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary from the CSV file where each letter is mapped to its phonetic code
# The iterrows() method allows us to iterate over each row in the DataFrame
dic = {row.letter: row.code for (index, row) in data.iterrows()}

# Function to handle user input and convert it to NATO phonetic code
def generate():
    # Asking the user to input a word and converting it to uppercase
    word = input("Enter a word: ").upper()
    
    try:
        # List comprehension: Iterating over each letter in the word and getting its corresponding NATO code
        result = [dic[letter] for letter in word]
        
        # Printing the list of phonetic alphabet codes corresponding to the letters in the word
        print(result)
        
    except KeyError:
        # If a KeyError occurs (e.g., user inputs a non-alphabetic character), print an error message
        print("Sorry, enter only characters from the alphabet please!")
        
        # Call the generate function again to allow the user to try again
        generate()

# Calling the generate function to start the process
generate()

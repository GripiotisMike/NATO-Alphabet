import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate():
    word = input("Enter a word: ").upper()
    try:
        result = [dic[letter] for letter in word]
        print(result)
    except KeyError:
        print("Sorry, enter only characters from the alphabet please!")
        generate()


generate()

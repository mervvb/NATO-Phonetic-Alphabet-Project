import pandas
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alph = pandas.DataFrame(data)
# print(nato_phonetic_alph)
new_alph = {row.letter: row.code for (index, row) in nato_phonetic_alph.iterrows()}
# print(new_alph)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        user_input_list = [new_alph[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_input_list)


generate_phonetic()

import pandas
# dict_nato = pandas.read_csv("nato_phonetic_alphabet.csv").set_index('letter').to_dict()
# nato = input("What word you want to decode into Nato Phonetic Alphabet ? ").upper()
# result = []
# for letter in nato:
#     if letter in dict_nato['code']:
#         result.append(dict_nato['code'][letter])
# print(result)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

try:
    output = [phonetic[letter] for letter in word]
except KeyError:
    print("Please enter only letters")
else:
    print(output)

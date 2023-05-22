from algorithm.scrabble import *
from db.txtToArray import *
import time

dictionary = dictionary_to_array("src\db\dictionary.txt")
point_char = point_to_array("src\db\point.txt")
available_char = input("Enter available characters: ")
# ex: CHATREB
rack_letters = input("Enter rack letters: ")
# ex: N jika ingin mencari possible words yang memiliki N
# ex: _N_ jika ingin mencari possible words yang memiliki N di tengah
# ex: _ jika ingin mengeluarkan all possible words
stringMatching = input("Enter string matching (bm/kmp): ")

start_time = time.time()
valid_words = scrabble(dictionary, available_char, rack_letters, point_char, stringMatching)
end_time = time.time()

print("Valid words:", valid_words)
# valid words sorting by point
print("Execution time:", end_time - start_time, "seconds")
# execution time
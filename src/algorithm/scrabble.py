from algorithm.bm import bm_match
from algorithm.bruteforce import bruteforce_match
from algorithm.kmp import kmp_match

def check_string_fit(string, characters):
    char_count = {}
    
    # Count the occurrences of each character in the characters set
    for char in characters:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check if the string can be formed using the characters set
    for char in string:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

def scrabble(dictionary, available_char, rack_letters, point_char, stringMatching):
    valid_words = []
    available_char = available_char.upper()
    rack_letters = rack_letters.upper()
    stringMatching = stringMatching.lower()
    indexChar = []
    for i in range(len(rack_letters)):
        if rack_letters[i] != '_' and rack_letters[i] != '/':
            indexChar.append([rack_letters[i], i])
    
    for element in indexChar:
        available_char += element[0] 
    chars = list(available_char)

    for rack in bruteforce_match(chars, indexChar, rack_letters):
        for word in dictionary:
            word = word.upper()
            if len(word) > len(available_char):
                continue
            if stringMatching == "bm":
                valid = bm_match(word,rack)
                if ((valid != -1) and (word not in valid_words) and (check_string_fit(word, available_char))):
                    valid_words.append(word)
            if stringMatching == 'kmp':
                valid = kmp_match(word,rack)
                if ((valid != -1) and (word not in valid_words) and (check_string_fit(word, available_char))):
                    valid_words.append(word)

    valid_words = sorted(valid_words, key=lambda w: sum([p[1] for p in point_char if p[0] in w]), reverse=True)
    return valid_words

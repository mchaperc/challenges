#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
from random import choice
from itertools import permutations

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letter():
    return choice(POUCH)


def draw_num_letters(num=7):
    return [(lambda: draw_letter())() for num in range(num)]


def possible_word_lengths(letters=[]):
    return [word_length for word_length in range(1, len(letters)+1)]


def generate_letter_combinations(letters=[], length=0):
    return [permutation for permutation in permutations(letters, length)]


def create_lowercase_word_from_letter_permutation(letter_permutation=[]):
    return ''.join(letter_permutation)


def determine_all_possible_word_permutations_from_drawn_letters(letters=[], word_lengths=[]):
    possible_words = []
    for length in word_lengths:
        letter_permutations = [permutation for permutation in permutations(letters, length)]
        for letter_permutation in letter_permutations:
            letter_combo = create_lowercase_word_from_letter_permutation(letter_permutation=letter_permutation)
            if letter_combo.lower() in DICTIONARY:
                possible_words.append(letter_combo)
    return possible_words


def contains_non_drawn_letters(word='', letters=[]):
    unallowed_letters = False
    for letter in word:
        if letter.upper() not in letters:
            unallowed_letters = True
    return unallowed_letters


def present_user_with_drawn_letters(letters):
    print(f"The letters that you drew are: {', '.join(letters)}")
    print("What is the word you wish to play from the drawn letters?")


def main():
    letters = draw_num_letters()

    present_user_with_drawn_letters(letters)

    user_word = input()

    while user_word.lower() not in DICTIONARY or contains_non_drawn_letters(user_word, letters):
        print("I'm sorry, but the word you've chosen is not in the dictionary, or it contains letters that you did not draw. Please try again:")
        present_user_with_drawn_letters(letters)
        user_word = input()

    user_word_value = calc_word_value(user_word)

    word_lengths = possible_word_lengths(letters=letters)
    max_word = max_word_value(determine_all_possible_word_permutations_from_drawn_letters(letters=letters, word_lengths=word_lengths))

    print(f"Your word was: {user_word}")
    print(f"The most valuable possible word was: {max_word}")
    print(f"Your score is: {(user_word_value / calc_word_value(max_word)) * 100}")


if __name__ == "__main__":
    main()

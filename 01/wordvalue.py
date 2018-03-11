from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY, 'r') as f:
        return [word.strip() for word in f.read().split()]

def calc_word_value(word):
    score = 0
    for letter in word:
        try:
            score += LETTER_SCORES[letter.upper()]
        except:
            pass
    return score

def max_word_value(words=load_words()):
    max_word = words[0]
    for word in words:
        if calc_word_value(word) > calc_word_value(max_word):
            max_word = word
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate

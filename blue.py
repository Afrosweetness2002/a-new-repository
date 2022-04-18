def character_score(character):
    return ord(character) - ord('a') + 1

def word_score(word):
    return sum(character_score(i) for i in word)

def find_max_score_word(word_string):
    return(max(word_string.split(), key=word_score))


print(find_max_score_word("hello world zazazazaza"))
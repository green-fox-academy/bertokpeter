def count_letters(word):
    letters = {}
    for i in word:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
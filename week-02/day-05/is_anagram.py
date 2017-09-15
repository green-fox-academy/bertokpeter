anagram1 = input("Please enter your first word here: ")
anagram2 = input("Please enter your second word here: ")
def string_to_list(text):
    length = len(text)
    word = []
    for i in range(length):
        word.append(text[i])
    return word
def is_anagram(tex1, text2):
    word1 = string_to_list(tex1)
    word2 = string_to_list(text2)
    if length1 == length2:
        sum = []
        for i in range(length1):
            if text1[i] in text2:
                sum.append(
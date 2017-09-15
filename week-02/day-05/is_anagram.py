anagram1 = input("Please enter your first word here: ")
anagram2 = input("Please enter your second word here: ")
def string_to_list(text):
    word = []
    for i in range(len(text)):
        word.append(text[i])
    return word
def is_anagram(tex1, text2):
    word1 = string_to_list(tex1)
    word2 = string_to_list(text2)
    if len(word1) == len(word2):
        for i in word1:
            if i in word2:
                word2.remove(i)
    if len(word2) == 0:
        print("The words are anagrams")
    else:
        print("These words aren't anagrams")
is_anagram(anagram1,anagram2)
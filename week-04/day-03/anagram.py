def anagram(text1, text2):
    if len(text1) == len(text2):
        word_list = []
        for i in text2:
            word_list.append(i)
        for i in text1:
            if i in word_list:
                word_list.remove(i)
            if len(word_list) == 0:
                return True
    return False
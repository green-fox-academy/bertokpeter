def anagram(text1, text2):
    if len(text1) == len(text2):
        new_text = ""
        for i in text1:
            if i in text2:
                new_text = new_text + i
            if len(text2) == len(new_text):
                return True
    return False
palindrome= input("Please enter your word here: ")
def string_to_list(text):
    word = []
    for i in range(len(text)):
        word.append(text[i])
    return word
def create_palindrome(palindrome):
    word_list = string_to_list(palindrome)
    length = len(word_list)
    while length > 0:
        palindrome = palindrome + word_list[length-1]
        length -= 1
    return palindrome
print(create_palindrome(palindrome))
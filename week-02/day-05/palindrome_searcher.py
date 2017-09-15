input_text = input("Please enter your text here: ")
def string_to_list(text):
    word = []
    for i in range(len(text)):
        word.append(text[i])
    return word
def create_palindrome(string):
    word_list = string_to_list(string)
    length = len(word_list)
    palindrome = ""
    while length > 0:
        palindrome = palindrome + word_list[length-1]
        length -= 1
    return palindrome
def palindrome_searcher(long_text):
    lowercase = long_text.lower()
    palindrome = create_palindrome(lowercase)
    length = len(lowercase)
    palindrome_list = []
    for i in range(length-2):
        for j in range(3,length + 1):
            if lowercase[i:i+j] == palindrome[length-(i+j):length-i]:
                palindrome_list.append(lowercase[i:i+j])
    return palindrome_list
print (palindrome_searcher(input_text))
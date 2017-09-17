input_text = input("Please enter your text here: ")
def reverse_string(text):
    return text[::-1]
def palindrome_searcher(long_text):
    lowercase = long_text.lower()
    palindrome = reverse_string(lowercase)
    length = len(lowercase)
    palindrome_list = []
    for i in range(length-2):
        for j in range(3,length+1):
            if lowercase[i:i+j] == palindrome[length-(i+j):length-i]:
                palindrome_list.append(lowercase[i:i+j])
    return palindrome_list
print (palindrome_searcher(input_text))
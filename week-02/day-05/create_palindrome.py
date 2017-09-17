palindrome= input("Please enter your word here: ")
def reverse_string(text):
    return text[::-1]
def create_palindrome(palindrome):
    reversed_word = reverse_string(palindrome)
    palindrome = palindrome + reversed_word
    return palindrome
print(create_palindrome(palindrome))
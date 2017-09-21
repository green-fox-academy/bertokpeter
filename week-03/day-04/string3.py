# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
try:
    def x_to_y(text):
        new_text = ""
        if len(text) == 1:
            return new_text + text[0]
        else:
            new_text = new_text + text[0] + "*" 
            return new_text + x_to_y(text[1:])

    print(x_to_y("My ex exited the xmen X times and x is so ixxy I feel like x"))
except TypeError:
    print("text must be string")
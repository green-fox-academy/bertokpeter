# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
try:
    def x_to_y(text):
        new_text = ""
        if len(text) == 0:
            return new_text
        else:
            if text[0] == "x":
                new_text = new_text + "y"
                return new_text + x_to_y(text[1:])
            else:
                new_text = new_text + text[0]
                return new_text + x_to_y(text[1:])

    print(x_to_y("My ex exited the xmen x times and x is so ixxy I feel like x"))
except TypeError:
    print("text must be string")
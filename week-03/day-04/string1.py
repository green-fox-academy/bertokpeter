# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_to_y(text):
    new_text = ""
    if not "x" in text:
        return new_text
    else:
        new_text = text.replace("x","y")
        return new_text

print(x_to_y("My ex exited the xmen x times"))
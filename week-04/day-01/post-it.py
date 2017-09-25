# Create a PostIt class that has
#   a background_color
#   a text on it
#   a text_color
# Create a few example post-it objects:
#   an orange with blue text: "Idea 1"
#   a pink with black text: "Awesome"
#   a yellow with green text: "Superb!"
class PostIt:
    background_color = ""
    text = ""
    text_color = ""

idea = PostIt()
idea.background_color = "orange"
idea.text = "Idea 1"
idea.text_color = "blue"

awesome = PostIt()
awesome.background_color = "pink"
awesome.text = "Awesome"
awesome.text_color = "black"

superb = PostIt()
superb.background_color = "yellow"
superb.text = "Superb!"
superb.text_color = "green"

print(superb.background_color + ", " + superb.text + ", " + superb.text_color)
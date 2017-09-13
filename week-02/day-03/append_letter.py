# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"
def create_new_verbs(verb_list, text):
    for i in range(len(verb_list)):
        verb_list[i] = text + verb_list[i]
    return verb_list
verbs = create_new_verbs(verbs,preverb)
print(verbs)
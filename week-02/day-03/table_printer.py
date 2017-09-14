# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]
def table_printer(ingredient_list):
    key_list = []
    for k in ingredient_list[0]:
        key_list.append(k)
    cooling_length = len(key_list[2])
    stock_length = len(key_list[1])
    name_list = []
    for i in ingredient_list:
        name_list.append(i["name"])
    max_length = len(max(name_list, key=len))
    print("+" + "-"*(max_length+2) + "+" + "-"*(cooling_length+2) + "+" + "-"*(stock_length+2) + "+")
    print("| Ingredient" + " "*(max_length+2-len(" Ingredient")) + "| Needs cooling | In stock |")
    print("+" + "-"*(max_length+2) + "+" + "-"*(cooling_length+2) + "+" + "-"*(stock_length+2) + "+")
    for i in ingredient_list:
        Yes = ""
        if i["needs_cooling"]:
            Yes = Yes + "Yes"
        else:
            Yes = Yes + "No"
        if i["in_stock"] == 0:
            i["in_stock"] = "-"
        print("| " + i["name"] + " "*(max_length-len(i["name"])+ 1) + "| " + Yes + " "*(cooling_length+1-len(Yes)) + "| " + str(i["in_stock"]) + " "*stock_length + "|")
    print("+" + "-"*(max_length+2) + "+" + "-"*(cooling_length+2) + "+" + "-"*(stock_length+2) + "+")
table_printer(ingredients)
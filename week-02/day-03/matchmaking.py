# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bozsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Bela", "Todd", "Neef", "Jeff"]
import random
order = []
while len(girls) > 0 or len(boys) > 0:
    if len(girls) > 0:
        number = random.randint(0,len(girls)-1)
        order.append(girls[number])
        girls.remove(girls[number])
    if len(boys) > 0:
        number = random.randint(0,len(boys)-1)
        order.append(boys[number])
        boys.remove(boys[number])
print(order)
# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bozsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Bela", "Todd", "Neef", "Jeff"]
import random
order = []
length_girls = len(girls)
length_boys = len(boys)
for i in range(length_girls + length_boys + 1):
    if i%2 == 0 and len(girls) > 0:
        number = random.randint(0,length_girls-i/2-1)
        order.append(girls[number])
        girls[number:number+1] = []
    if i%2 == 1 and len(boys) > 0:
        number = random.randint(0,length_boys-(i//2)-1)
        order.append(boys[number])
        boys[number:number+1] = []
print(order)
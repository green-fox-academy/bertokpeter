students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average
def got_more(student_list):
    for i in student_list:
        if i["candies"] > 4:
            print(i["name"] + "has got more than 4 candies")
got_more(students)
def average(student_list):
    candies_sum = []
    for i in student_list:
        candies_sum.append(i["candies"])
    return sum(candies_sum)/len(candies_sum)
sum_of_candies = average(students)
print(sum_of_candies)
students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies
def candy_counter(student_list):
    for i in student_list:
        student = ""   
        student = student + i["name"] + " owns " + str(i["candies"]) + " candies"
        print(student)
candy_counter(students)
def sum_age(student_list):
    ages = []
    for i in student_list:
        if i["candies"] < 5:
            ages.append(i["age"])
    return sum(ages)
ages_of_students = sum_age(students)
print(ages_of_students)
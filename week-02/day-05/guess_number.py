import random
random_range = int(input("Enter the biggest number you would like to guess: "))
def guess(range):
    number = random.randint(1,range)
    lives = int(input("How many lives do you want? "))
    print("I've the number between 1-" + str(range) + ". You have " + str(lives) + " lives.")
    a = int(input("Can you guess the number? "))
    while a != number and lives > 0:
        print("Guess again... ")
        lives -= 1
        if lives == 0:
            print("Sorry you died. Better luck next time!")
        elif a < number:
            print("Too low. You've " + str(lives) + "lives left.")
            a = int(input("Can you guess the number? "))
        else:
            print("Too high. You've " + str(lives) + "left.")
            a = int(input("Can you guess the number? "))
    if a == number:
        print("Congratulations! You found the number: " + str(number))
guess(random_range)
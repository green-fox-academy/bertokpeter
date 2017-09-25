from domino import Domino
import random

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

print(dominoes)

def create_snake(dominoes_list):
    snake = []
    snake.append(random.sample(dominoes_list, 1)[0])
    while len(snake) < len(dominoes_list):
        for domino in dominoes_list:
            if len(snake) == len(dominoes_list):
                pass
            elif domino.values[0] == snake[len(snake)-1].values[1]:
                snake.append(domino)
    return snake

print(create_snake(dominoes))
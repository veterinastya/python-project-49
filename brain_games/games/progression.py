import random
from random import randint

RULES = 'What number is missing in the progression?'

def game_data():
    list_length = randint(5, 15)
    start = randint(1, 10)
    step = randint(1, 10)
    correct_answer, question = create_progression(start, list_length, step)
    return correct_answer, question

def create_progression(start, list_length, step):
    progression_list = []
    stop = start + step * list_length
    for value in range(start, stop, step):
        progression_list.append(value)
    missing_index = randint(0, list_length - 1)
    missing_number = progression_list[missing_index]
    correct_answer = missing_number
    progression_list[missing_index] = '..'
    question = str(progression_list)
    
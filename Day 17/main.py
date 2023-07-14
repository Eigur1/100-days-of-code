from data import question_data as qd
from quiz_brain import create_question, is_there_answer
import random

quiz_directory = []
for question in qd:
    qf = create_question(question)
    quiz_directory.append(qf)
numq = 0
score = 0
while is_there_answer(quiz_directory):
    numq += 1
    q = quiz_directory.pop(random.randint(0, len(quiz_directory) - 1))
    answ = input(f"Q{numq} = {q.question}. (True/False): ")

    if answ == q.answer:
        score += 1
        print(f"You got it right!\n The correct answer was: {q.answer} \n Your current score is {score}/{numq}.")
    else:
        print(
            f"Wrong! You fucking whore!\n The correct answer was: {q.answer} \n Your current score is {score}/{numq}.")
    numq += 1
print(f"End bitch, final score was {score}/{numq}.")

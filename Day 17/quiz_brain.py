from question_model import Question
from data import question_data

def create_question(quiz_data):
    question = quiz_data["text"]
    answer = quiz_data["answer"]
    question_final = Question(question,answer)
    return question_final

def is_there_answer(quest_list):
    if len(quest_list) > 0:
        return True
    else:
        return False

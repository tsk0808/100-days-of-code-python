#   text, answer Variable 가짐
from question_model import Question


#   Text 형태의 Dictionary 가짐
from data import question_data


#   question_number,
#   question_list,
#   score Member Variable 가짐


from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Thanks for completing that!\nYour final score is: {quiz.score}/{quiz.question_number}")

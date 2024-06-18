from question_model import Question
from data import question_data as qd
from quiz_brain import QuizBrain
question_bank = []
for questions in qd:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while not quiz.still_has_questions():
    quiz.next_question()
print('You have completed the quiz! Congratulations.')
print(f"Your final score was {quiz.score}/{quiz.question_number}")

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_q = Question(question, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_q()
else:
    print("Quiz finished.")
    print(f"Your final score was {quiz.score} / {quiz.q_number}")

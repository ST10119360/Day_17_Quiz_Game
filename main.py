from Questions import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

new_q = QuizBrain(question_bank)
total = 0
end_game = False

while new_q.still_has_questions() and not end_game:
    new_q.next_question()


print("End of the game.")

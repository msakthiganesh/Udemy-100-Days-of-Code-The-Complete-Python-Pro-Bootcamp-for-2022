from question_model import Question
from data import question_data, open_trivia_db_questions
from quiz_brain import QuizBrain

question_choice = input("Choose your topic of interest: QuestionData or OpenTrivia: ").lower()
if question_choice == "questiondata":
    question_bank = [Question(item["text"], item["answer"]) for item in question_data]
else:
    question_bank = [Question(item["question"], item["correct_answer"]) for item in open_trivia_db_questions]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

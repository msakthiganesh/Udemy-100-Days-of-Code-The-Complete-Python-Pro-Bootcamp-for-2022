class QuizBrain:

    def __init__(self, question_list: list, question_number: int = 0, score: int = 0):
        self.question_list = question_list
        self.question_number = question_number
        self.score = score

    def next_question(self):
        current_question = self.question_list[self.question_number].question
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question}?: ")
        self.check_answer(user_answer, current_answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer is {current_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

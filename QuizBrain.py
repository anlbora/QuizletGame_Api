import random
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return self.current_question

    def check_answer(self, user_answer):
        correct_answer = self.current_question["correct_answer"]
        if self.current_question["type"] == "multiple":
            # For multiple choice, accept the option number as well as the full answer
            options = self.current_question["incorrect_answers"] + [self.current_question["correct_answer"]]
            random.shuffle(options)
            try:
                selected_option = int(user_answer)
                if 1 <= selected_option <= len(options):
                    return options[selected_option - 1].lower() == correct_answer.lower()
            except ValueError:
                return user_answer.lower() == correct_answer.lower()
        return user_answer.lower() == correct_answer.lower()
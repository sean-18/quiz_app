import html
from data import GetData
class QuizBrain(GetData):

    def __init__(self):
        GetData.__init__(self)
        self.q_obj = GetData()
        self.q_obj.get_new_data()
        self.question_number = 0
        self.score = 0
        self.question_list = self.q_obj.question_bank
        self.current_question = None
        try:
            with open('highscore.txt') as file:
                self.curr_hs = file.readline()
        except FileNotFoundError:
            with open('highscore.txt', 'w') as f:
                self.curr_hs = 0
                f.write(f"{self.curr_hs}")


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question=html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question}"
        #user_answer = input(f"Q.{self.question_number}: {question} (True/False): ")
        #self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def highscore(self):
        if self.score > int(self.curr_hs):
            with open("highscore.txt", 'w') as filee:
                filee.write(f"{self.score}")
                self.curr_hs = self.score


    def retry(self):
        self.q_obj.question_bank.clear()
        self.q_obj.get_new_data()
        self.question_number = 0
        self.score = 0

        #print(self.q_obj.question_bank)




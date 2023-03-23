import requests
from question_model import Question

class GetData:
    def __init__(self):
        self.question_data = None
        self.question_bank = []
        #self.get_new_data()


    def get_new_data(self):
        self.question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean").json()["results"]
        #print(self.question_data)
        for question in self.question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_bank.append(new_question)
        #print(self.question_bank)

from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class Interface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.config(bg=THEME_COLOR,padx=20,pady=20)
        self.screen.title("Quiz")
        self.score_label=Label(text=f"score:{self.quiz.score}",bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1)

        self.highscore_label = Label(text=f"highscore:{self.quiz.curr_hs}", bg=THEME_COLOR, fg="white")
        self.highscore_label.grid(row=0, column=0)

        self.canvas=Canvas(height=250,width=300,highlightthickness=0,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="hello",width=280,font=('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,pady=50,columnspan=2)

        self.button_tick = Button()
        tick_image = PhotoImage(file="images/true.png")
        self.button_tick = Button(command =self.press_true ,image=tick_image,highlightthickness=0)
        self.button_tick.grid(row=2,column=0)

        self.button_wrong = Button()
        wrong_image = PhotoImage(file="images/false.png")
        self.button_wrong = Button(command = self.press_false ,image=wrong_image, highlightthickness=0)
        self.button_wrong.grid(row=2, column=1)

        self.get_question()
        self.screen.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score:{self.quiz.score}")
            questions=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=questions)
        else:
            self.quiz.highscore()
            self.canvas.itemconfig(self.question_text,text=f"FINAL SCORE {self.quiz.score}\nRESTART?")
            self.button_tick.config(command=self.restart)
            self.button_wrong.config(state="disabled")
    def press_true(self):
        self.display(self.quiz.check_answer("True"))

    def press_false(self):
        self.display(self.quiz.check_answer("False"))

    def display(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000, self.get_question)

    def restart(self):
        self.quiz.retry()
        self.get_question()
        self.button_tick.config(command=self.press_true)
        self.button_wrong.config(state="active",command=self.press_false)





import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial",16,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")
        self.right = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right.grid(row=2, column=0)
        self.wrong = tk.Button(image=false_image, highlightthickness=0, command=self.wrong_pressed)
        self.wrong.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="It's the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
        self.canvas.config(bg="white")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.show_answer(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.show_answer(is_right)

    def show_answer(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
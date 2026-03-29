from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("How Well Do You Know Me?")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200,
            150,
            width=320,
            text="Welcome to the quiz!",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(text="True", width=12, font=("Arial", 14, "bold"), command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(text="False", width=12, font=("Arial", 14, "bold"), command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_result_message(self):
        if self.quiz.score >= 8:
            return f"Your final score is {self.quiz.score}/{len(self.quiz.question_list)}.\nYou are my close friend."
        elif self.quiz.score >= 5:
            return f"Your final score is {self.quiz.score}/{len(self.quiz.question_list)}.\nYou know me fairly well."
        else:
            return f"Your final score is {self.quiz.score}/{len(self.quiz.question_list)}.\nYou are not as close as you think."

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.get_result_message())
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
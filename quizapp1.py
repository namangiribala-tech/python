import tkinter as tk
from tkinter import messagebox

# Quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "N2"],
        "answer": "H2O"
    },
    {
        "question": "What is the fastest land animal?",
        "options": ["Cheetah", "Lion", "Tiger", "Elephant"],
        "answer": "Cheetah"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x300")

        self.question_index = 0
        self.score = 0

        # Question label
        self.question_label = tk.Label(root, text="", wraplength=350, justify="center", font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Radio buttons for options
        self.radio_var = tk.StringVar()
        self.radio_buttons = [tk.Radiobutton(root, text="", variable=self.radio_var, value="", font=("Arial", 12)) for _ in range(4)]
        for rb in self.radio_buttons:
            rb.pack(anchor="w", padx=20)

        # Next button
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        question_data = quiz_data[self.question_index]
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.radio_buttons[i].config(text=option, value=option)

        self.radio_var.set("")

    def next_question(self):
        selected_answer = self.radio_var.get()
        correct_answer = quiz_data[self.question_index]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.question_index += 1

        if self.question_index < len(quiz_data):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your score is {self.score} out of {len(quiz_data)}")
        self.root.quit()

# Create the main window
root = tk.Tk()

# Create the QuizApp object
app = QuizApp(root)

# Start the Tkinter event loop
root.mainloop()

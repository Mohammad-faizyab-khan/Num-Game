import tkinter as tk
import random

def is_valid_char(char):
    return char.isdigit()

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.number_to_guess = random.randint(1, 100)

        self.master.geometry("300x200")
        self.master.configure(bg='lightblue')

        tk.Label(master, text="Welcome to Number Guessing Game!", bg='lightblue').pack()
        tk.Label(master, text="Guess a number between 1 and 100", bg='lightblue').pack()

        validate_command = master.register(is_valid_char)
        self.guess_entry = tk.Entry(master, validate="key", validatecommand=(validate_command, '%S'))
        self.guess_entry.insert(0, "Enter your guess here")
        self.guess_entry.pack(pady=10)

        self.result_label = tk.Label(master, text="", bg='lightblue')
        self.result_label.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.master.bind('<Return>', self.check_guess)

    def check_guess(self, event=None):
        user_guess = int(self.guess_entry.get())
        if user_guess > self.number_to_guess:
            self.result_label['text'] = "Too high!"
        elif user_guess < self.number_to_guess:
            self.result_label['text'] = "Too low!"
        else:
            self.result_label['text'] = "Congratulations! You guessed correctly."

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# Question 1
def printData(filename):
    try:
        with open(filename, 'r') as input_file:
            data = input_file.read()
            if not data:
                raise ValueError('No data available')
            else:
                lines = data.split('\n')
                for line in lines:
                    values = line.split(",")
                    print(values[0], ",", values[1])
    except IOError as e:
        logging.exception(e)
    return data

printData("customers.csv")

# Question 2
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ScoreIsLessException(Error):
    def __init__(self):
        self.message = "This score is too low. You failed the exam"
        super().__init__(self.message)

    def __str__(self):
        return self.message

number = 50

try:
    i_num = int(input("Enter a number: "))
    if i_num < number:
        raise ScoreIsLessException()
    print("You passed the exam. Congratulations.")
except ScoreIsLessException as e:
    print(e)

# Question 3
from tkinter import *

class info(Frame):

    def __init__(self):
        self.window = Tk()

        self.new_frame = Frame(self.window, width=450, height=50, padx=50, pady=30)

        self.new_frame.grid(row=5, sticky="nsew")

        self.name = '\tSteven Marcus\n\t274 Bally Drive\n\tWaynesville, NC 27999'

        self.l1 = Label(self.new_frame, text='\n\n')

        self.l1.grid(row=0, column=1)

        self.show_info_button = Button(self.new_frame, text="Show Info", command=self.show_info)

        self.show_info_button.grid(row=8, column=1, padx=20, pady=30)

        self.quit = Button(self.new_frame, text='Quit', command=self.quit_window)

        self.quit.grid(row=8, column=4, padx=20, pady=30)

        self.window.mainloop()

    def show_info(self):
        self.l1['text'] = self.name

    def quit_window(self):
        self.window.destroy()

info()

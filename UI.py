import tkinter as tk
from Calculator import calculator
from tools import transcription

class UI:
    def __init__(self, ):
        self.screen = tk.Tk()
        self.screen.title("Calculator")

        self.entry = tk.Entry(self.screen, width=20, font=("Arial", 16), bd=5, insertwidth=4, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            "(", ")", "+/-", "C",
            "7", "8", "9", "",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        self.rowValue = 1
        self.columnValue = 0

        self.setUpButtons()

        self.strResult = ""
        self.result = 0

    def calculate(self):
        tradInput = transcription(self.strResult[:-1])
        self.result = calculator(tradInput)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.result) + " ")
        self.strResult = str(self.result) + " "

    def addChar(self, char):
        if char == "-":
            self.strResult += "+ -"
            self.entry.insert(tk.END, "- ")
        elif char == "+/-":
            self.strResult += "-"
            self.entry.insert(tk.END, "-")
        elif char == ".":
            self.strResult = self.strResult[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.strResult)
            self.strResult += "."
            self.entry.insert(tk.END, ".")
        else:
            if len(self.strResult) > 1 and self.strResult[len(self.strResult) - 2] in "0123456789":
                self.strResult = self.strResult[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.strResult)
                self.strResult += char + "  "
                self.entry.insert(tk.END, char + "  ")
            else: 
                self.strResult += char + " "
                self.entry.insert(tk.END, char + " ")

    def deleteChar(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.strResult)
        self.strResult = ""

    def setUpButtons(self):
        for button in self.buttons:
            if button == "=":
                tk.Button(self.screen, text=button, width=10, height=2, command=lambda: self.calculate()).grid(row=self.rowValue, column=self.columnValue)
            elif button == "C":
                tk.Button(self.screen, text=button, width=10, height=2, command=lambda: self.deleteChar()).grid(row=self.rowValue, column=self.columnValue)
            else:
                tk.Button(self.screen, text=button, width=10, height=2, command=lambda button=button: self.addChar(button)).grid(row=self.rowValue, column=self.columnValue)
            
            self.columnValue += 1
            if self.columnValue == 4:
                self.columnValue = 0
                self.rowValue += 1

    def run(self):
        self.screen.mainloop()
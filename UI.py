import tkinter as tk
from Calculator import calculator
from tools import transcription

class UI:
    """
    Cette classe représente l'interface utilisateur de l'application calculatrice.
    Elle fournit des méthodes pour configurer l'interface utilisateur, gérer les clics sur les boutons et effectuer des calculs.
    """

    def __init__(self, ):
        self.screen = tk.Tk()
        self.screen.title("Calculatrice")

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
        """
        Calcule le résultat de l'expression saisie par l'utilisateur.
        """
        tradInput = transcription(self.strResult[:-1])
        self.result = calculator(tradInput)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.result) + " ")
        self.strResult = str(self.result) + " "

    def addChar(self, char):
        """
        Ajoute un caractère à l'expression saisie par l'utilisateur.

        Paramètres:
        - char: Le caractère à ajouter.
        """
        if char == "-":
            self.strResult += "+ -"
            self.entry.insert(tk.END, "- ")
        elif char == "+/-":
            self.strResult += "-"
            self.entry.insert(tk.END, "-")
        elif char == ".":
            self.strResult = self.strResult[:-1]
            self.strResult += "."
            self.entry.insert(tk.END, ".")
        else:
            self.strResult += char + " "
            self.entry.insert(tk.END, char + " ")

    def deleteChar(self):
        """
        Supprime le dernier caractère de l'expression saisie par l'utilisateur.
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.strResult)
        self.strResult = ""

    def setUpButtons(self):
        """
        Sets up the buttons on the calculator UI and assigns their respective functions.
        """
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
        """
        Runs the calculator application.
        """
        self.screen.mainloop()
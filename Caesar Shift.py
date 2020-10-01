import tkinter
from tkinter import *
from tkinter import ttk

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

    def createwidgets(self):
        self.c1 = ttk.Combobox(values=["Message"], width = 100)
        self.c1.pack(side="top")

        self.c2 = ttk.Combobox(values=["Shift"])
        self.c2.pack(side="top")

        self.start1 = Button(self, fg="darkblue", bg="white")
        self.start1["text"] = "CONVERT"
        self.start1["command"] = self.convert
        self.start1.pack(side="top")

        self.help = Button(self, fg="darkblue", bg="white")
        self.help["text"] = "Help"
        self.help["command"] = self.printhelp
        self.help.pack(side="top")

    def printhelp(self):
        print("Type your message into the first box (no spaces).")
        print("This can be an original message, or an already enciphered one.")
        print("Enter the magnitude of the Caesar shift into the second box.")
        print("If you want to decipher a message, enter a negative number.")
        print("|magnitude| < 26")

    def convert(self):
        string = window.c1.get()
        string.strip()
        string.lower()
        shift = window.c2.get()
        shift = int(shift)

        print("ENTERED: " + string)

        letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        part1 = []
        n = 0
        while (n < len(string)):
            part1.append(letters[string[n]])
            n = n + 1

        part2 = ""
        n = 0
        while (n < len(part1)):
            if ((part1[n] + shift) > 26):
                new = (part1[n] + shift) - 26
            else:
                new = part1[n] + shift
            new = numbers[new - 1]
            part2 = part2 + new
            n = n + 1

        print("CONVERTED: " + part2)


print("CAESAR SHIFT")
window = App()
window.master.title("Caesar Shift")
window.master.maxsize(1000, 500)
window.createwidgets()

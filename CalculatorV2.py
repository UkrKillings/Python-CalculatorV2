from tkinter import *

print("Развлекуха от by UkrKillent")

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFBA00")
        self.lbl.place(x=11, y=50)

        btns = [
            "В 0", "Нафиг", "*", "На 2",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "="
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFFF00",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "В 0":
            self.formula = ""
        elif operation == "Нафиг":
            self.formula = self.formula[0:-1]
        elif operation == "На 2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "Готовка":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Амеикански Калькулятор by UkrKillent")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
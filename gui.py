from tkinter import *
from time import sleep
import game

directions = ('w', 'a', 's', 'd')
window_sizes = {3: '263x263', 4: '350x350'}


class Gui:
    def __init__(self):
        self.master = Tk()
        self.master.resizable(0, 0)
        self.master.geometry(window_sizes[game.size])
        self.master.title("Nico's 8's game")

        self.bg_color = '#6c7b95'
        self.cell_color = '#8bbabb'

        self.master.config(bg=self.bg_color)

        self.cells = []
        for i in range(game.size ** 2):
            new_button = Label(self.master, bg=self.cell_color, font=('Arial', 44), foreground='#F9FFEE')
            new_button.place(heigh=85, width=85, x=2 + (85 + 2)*(i % game.size), y=2 + (85 + 2)*int(i / game.size))
            self.cells.append(new_button)
        self.update()

        self.master.bind('<Key>', self.button_pressed)
        self.master.bind('<space>', self.ai)
        self.master.bind('<Button-3>', self.clean)

    def update(self):
        table = [item for sublist in game.test.table for item in sublist]
        for i in range(game.size ** 2):
            if table[i] != 0:
                self.cells[i].config(text=table[i], bg=self.cell_color)
            else:
                self.cells[i].config(text=' ', bg=self.bg_color)
        self.master.update_idletasks()

    def clean(self, event):
        game.test.__init__(table='initial')
        self.update()

    def button_pressed(self, event):
        if event.char in directions:
            game.test.move(direction=event.char)
            self.update()
        elif event.char in {'3', '4'}:
            self.master.destroy()
            game.size = int(event.char)
            game.test.__init__(table='initial')
            self.__init__()

    def ai(self, event):
        steps = game.test.solver()
        for direction in steps:
            game.test.move(direction=direction)
            self.update()
            sleep(1)

my_gui = Gui()
my_gui.master.mainloop()
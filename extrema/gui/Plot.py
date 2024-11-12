from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure


class Plot:
    master = None
    interface = None

    frame = None

    def __init__(self, master, interface):
        self.master = master
        self.interface = interface

    def create(self):
        fig = Figure(figsize=(8, 5),
                     dpi=120)
        y = [i ** 2 for i in range(101)]
        plot1 = fig.add_subplot(111)
        plot1.plot(y)

        self._create_plot(fig)

    def update(self):
        a = self.interface.get__current_plot()
        self._create_plot(a)

    def _create_plot(self, data):
        if self.frame is not None:
            self.frame.destroy()
        self.frame = Frame(self.master, relief="groove", borderwidth=1)
        self.frame.grid(row=0, column=2)

        canvas = FigureCanvasTkAgg(data, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self.frame)
        toolbar.update()
        canvas.get_tk_widget().pack()

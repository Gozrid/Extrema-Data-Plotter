import tkinter
from tkinter import Label, Entry, Button


class PlotNaming:
    master = None
    interface = None

    title = None
    x_label = None
    y_label = None

    def __init__(self, master, interface):
        self.master = master
        self.interface = interface

        self.title = tkinter.StringVar(None)
        self.x_label = tkinter.StringVar(None)
        self.y_label = tkinter.StringVar(None)

    def create(self):
        Label(self.master, text='Plot naming', font='bold').grid(row=0, column=0, sticky='w')

        Label(self.master, text='Title of the plot').grid(row=1, column=0)
        Label(self.master, text='X-Axis labeling').grid(row=2, column=0)
        Label(self.master, text='Y-Axis labeling').grid(row=3, column=0)

        Entry(self.master, textvariable=self.title).grid(row=1, column=1)
        Entry(self.master, textvariable=self.x_label).grid(row=2, column=1)
        Entry(self.master, textvariable=self.y_label).grid(row=3, column=1)

        Button(self.master, text='Set', command=self._set_settings).grid(row=7, column=1)

    def _set_settings(self):
        self.interface.set__plot_title(self.title.get())
        self.interface.set__plot_x_axis(self.x_label.get())
        self.interface.set__plot_y_axis(self.y_label.get())

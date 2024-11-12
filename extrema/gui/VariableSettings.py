import tkinter
from tkinter import *


class VariableSettings:
    interface = None

    master = None

    maxima_height = None
    minima_height = None
    prominence = None
    distance_between_extremas_x = None
    start_time = None
    end_time = None
    precision = None

    def __init__(self, data_interface, master, maxima_height, minima_height, prominence, n, start_time, end_time,
                 precision):
        self.interface = data_interface
        self.master = master
        self.maxima_height = tkinter.StringVar(value=maxima_height)
        self.minima_height = tkinter.StringVar(value=minima_height)
        self.prominence = tkinter.StringVar(value=prominence)
        self.distance_between_extremas_x = tkinter.StringVar(value=n)
        self.start_time = tkinter.StringVar(value=start_time)
        self.end_time = tkinter.StringVar(value=end_time)
        self.precision = tkinter.StringVar(value=precision)

    def create(self):
        Label(self.master, text='Extrema analysis settings', font='bold').grid(row=0, column=0, sticky='w')

        Label(self.master, text='maxima_height').grid(row=1, column=0)
        Label(self.master, text='minima_height').grid(row=2, column=0)
        Label(self.master, text='prominence').grid(row=3, column=0)
        Label(self.master, text='distance_between_extremas_x').grid(row=4, column=0)
        Label(self.master, text='start_time').grid(row=5, column=0)
        Label(self.master, text='end_time').grid(row=6, column=0)
        Label(self.master, text='precision').grid(row=7, column=0)

        Entry(self.master, textvariable=self.maxima_height).grid(row=1, column=1)
        Entry(self.master, textvariable=self.minima_height).grid(row=2, column=1)
        Entry(self.master, textvariable=self.prominence).grid(row=3, column=1)
        Entry(self.master, textvariable=self.distance_between_extremas_x).grid(row=4, column=1)
        Entry(self.master, textvariable=self.start_time).grid(row=5, column=1)
        Entry(self.master, textvariable=self.end_time).grid(row=6, column=1)
        Entry(self.master, textvariable=self.precision).grid(row=7, column=1)

        Button(self.master, text='Set', command=self.set_settings).grid(row=8, column=1)

        self.set_settings()

    def set_settings(self):
        self.interface.set__distance(float(self.distance_between_extremas_x.get()))
        self.interface.set__prominence(float(self.prominence.get()))
        self.interface.set__end_time(float(self.end_time.get()))
        self.interface.set__start_time(float(self.start_time.get()))
        self.interface.set__maxima_height(float(self.maxima_height.get()))
        self.interface.set__minima_height(float(self.minima_height.get()))
        self.interface.set__precision(int(self.precision.get()))

    def get__maxima_height(self):
        return self.maxima_height.get()

    def get__minima_height(self):
        return self.minima_height.get()

    def get__prominence(self):
        return self.prominence.get()

    def get__n(self):
        return self.distance_between_extremas_x.get()

    def get__start_time(self):
        return self.start_time.get()

    def get__end_time(self):
        return self.end_time.get()

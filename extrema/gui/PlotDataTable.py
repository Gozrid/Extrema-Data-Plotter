import tkinter
from tkinter import Entry, END, Frame, Label


class PlotDataTable:
    master = None
    interface = None

    frame_min = None
    frame_max = None
    frame_speed = None

    min = None
    max = None

    def __init__(self, master, interface):
        self.master = master
        self.interface = interface

    def create(self):
        self.update()

    def update(self):
        if self.frame_speed is not None:
            self.frame_speed.destroy()
        self.frame_speed = Frame(self.master, relief="groove", borderwidth=1)
        self.frame_speed.grid(row=0, column=0, columnspan=2)

        if self.frame_min is not None:
            self.frame_min.destroy()
        self.frame_min = Frame(self.master, relief="groove", borderwidth=1)
        self.frame_min.grid(row=1, column=0)

        if self.frame_max is not None:
            self.frame_max.destroy()
        self.frame_max = Frame(self.master, relief="groove", borderwidth=1)
        self.frame_max.grid(row=1, column=1)

        data_list = self.interface.get__data_list()
        minima_list = self.interface.get__minima_extrema()
        maxima_list = self.interface.get__maxima_extrema()

        if len(minima_list) > 0:
            speed_minima = tkinter.StringVar(value=self.interface.get__speed_minima())
            Label(self.frame_speed, text='Minima speed').grid(row=0, column=2)
            Entry(self.frame_speed, textvariable=speed_minima).grid(row=0, column=3)

            time_minima_list = [['Time (Min.)'], ['Minima']]
            time_minima_list[0].extend(self._to_minutes(minima_list))
            for i in range(len(minima_list)):
                time_minima_list[1].append(data_list[minima_list[i]])

            for i in range(len(time_minima_list[0])):
                for j in range(len(time_minima_list)):
                    self.min = Entry(self.frame_min)
                    self.min.grid(row=i, column=j)
                    self.min.insert(END, time_minima_list[j][i])

        if len(maxima_list) > 0:
            speed_maxima = tkinter.StringVar(value=self.interface.get__speed_maxima())
            Label(self.frame_speed, text='Maxima speed').grid(row=0, column=0)
            Entry(self.frame_speed, textvariable=speed_maxima).grid(row=0, column=1)

            time_maxima_list = [['Time (Min.)'], ['Maxima']]
            time_maxima_list[0].extend(self._to_minutes(maxima_list))
            for i in range(len(maxima_list)):
                time_maxima_list[1].append(data_list[maxima_list[i]])

            for i in range(len(time_maxima_list[0])):
                for j in range(len(time_maxima_list)):
                    self.max = Entry(self.frame_max)
                    self.max.grid(row=i, column=j)
                    self.max.insert(END, time_maxima_list[j][i])

    def _to_minutes(self, time_list):
        new_time_list = []
        for time in time_list:
            new_time_list.append(round(time, 2))

        return new_time_list

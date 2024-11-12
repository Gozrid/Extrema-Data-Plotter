import csv
from tkinter import Button

from tkinter import filedialog as fd


class PlotAction:
    master = None
    interface = None
    gui = None

    def __init__(self, master, interface, gui):
        self.master = master
        self.interface = interface
        self.gui = gui

    def create(self):
        Button(self.master, text='Plot!', command=self._plot_action, height=3, width=15).grid(row=0, column=0)
        Button(self.master, text='Save extrema to csv!', command=self._save_as_csv, height=3, width=15).grid(row=0,
                                                                                                             column=1)

    def _plot_action(self):
        self.interface.create__debug_plot_image()
        self.interface.create__plot_image()
        self.gui.update_plots()

    def _save_as_csv(self):
        file_path = fd.asksaveasfilename(filetypes=[('CSV Files', '*.csv')], initialdir='.', defaultextension='.csv',
                                         confirmoverwrite=True, initialfile='extremas.csv')

        data_list = self.interface.get__data_list()
        minima_list = self.interface.get__minima_extrema()
        maxima_list = self.interface.get__maxima_extrema()

        if len(minima_list) > 0 or len(maxima_list) > 0:
            time_minima_list = []
            time_maxima_list = []

            if len(minima_list) > 0:
                time_minima_list = [['Time seconds'], ['Time minutes'], ['Minima']]
                time_minima_list[0].extend(minima_list)
                time_minima_list[1].extend(self._to_minutes(minima_list))
                for i in range(len(minima_list)):
                    time_minima_list[2].append(data_list[minima_list[i]])

            if len(maxima_list) > 0:
                time_maxima_list = [['Time seconds'], ['Time minutes'], ['Maxima']]
                time_maxima_list[0].extend(maxima_list)
                time_maxima_list[1].extend(self._to_minutes(maxima_list))
                for i in range(len(maxima_list)):
                    time_maxima_list[2].append(data_list[maxima_list[i]])

            with open(file_path, 'w') as f:
                if len(minima_list) > 0 and (
                        len(maxima_list) <= 0 or len(time_minima_list[0]) > len(time_maxima_list[0])):
                    size = len(time_minima_list[0])
                else:
                    size = len(time_maxima_list[0])

                for i in range(size):
                    write = csv.writer(f)

                    local_list = []
                    if len(time_minima_list) > 0 and i < len(time_minima_list[0]):
                        local_list.append(time_minima_list[0][i])
                        local_list.append(time_minima_list[1][i])
                        local_list.append(time_minima_list[2][i])

                    if len(time_maxima_list) > 0 and i < len(time_maxima_list[0]):
                        local_list.append(time_maxima_list[0][i])
                        local_list.append(time_maxima_list[1][i])
                        local_list.append(time_maxima_list[2][i])

                    write.writerow(local_list)

    def _to_minutes(self, time_list):
        new_time_list = []
        for time in time_list:
            new_time_list.append(round(time, 2))

        return new_time_list

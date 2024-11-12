import pandas as pd
from matplotlib.figure import Figure


class DataPlotter:
    minima_list = []
    maxima_list = []

    title = 'Werte <-> Zeit'
    x_axis = 'Zeit in Minuten'
    y_axis = 'Werte'

    def set__title(self, title):
        self.title = title

    def set__x_axis(self, x_axis):
        self.x_axis = x_axis

    def set__y_axis(self, y_axis):
        self.y_axis = y_axis

    def set__minima_list(self, minima_list):
        self.minima_list = minima_list

    def set__maxima_list(self, maxima_list):
        self.maxima_list = maxima_list

    def get__minima_list(self):
        return self.minima_list

    def get__maxima_list(self):
        return self.maxima_list

    def debug_plot(self, time_list, data_list, start_time, end_time):
        figure = Figure(figsize=(5, 5), dpi=70)
        sub_plot = figure.add_subplot(111)

        dataframe = pd.DataFrame({'data': data_list})

        timestamps = self._to_minutes(time_list)

        sub_plot.plot(dataframe['data'])
        sub_plot.plot(self.maxima_list, dataframe['data'][self.maxima_list], "x")
        sub_plot.plot(self.minima_list, dataframe['data'][self.minima_list], "x", c="r")
        sub_plot.set_xticks(dataframe.index, timestamps, rotation=23)
        sub_plot.locator_params(axis='x', nbins=9)
        sub_plot.set_xlabel(self.x_axis)
        sub_plot.set_ylabel(self.y_axis)
        sub_plot.set_title(self.title)

        if start_time != 0:
            index_start_time = list.index(time_list, start_time)
            sub_plot.axvline(index_start_time, color='r')

        if end_time != 0:
            index_end_time = list.index(time_list, end_time)
            sub_plot.axvline(index_end_time, color='orange')

        # figure.show()
        return figure

    def plot(self, time_list, data_list):
        figure = Figure(figsize=(8, 5), dpi=120)
        sub_plot = figure.add_subplot(111)

        dataframe = pd.DataFrame({'data': data_list})

        timestamps = self._to_minutes(time_list)

        sub_plot.plot(dataframe['data'])
        sub_plot.set_xticks(dataframe.index, timestamps, rotation=23)
        sub_plot.locator_params(axis='x', nbins=9)
        sub_plot.set_xlabel(self.x_axis)
        sub_plot.set_ylabel(self.y_axis)
        sub_plot.set_title(self.title)

        return figure

    def _to_minutes(self, time_list):
        new_time_list = []
        for time in time_list:
            new_time_list.append(round(time, 2))

        return new_time_list

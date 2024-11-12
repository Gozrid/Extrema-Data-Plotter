from extrema.data.DataExtremaFinder import DataExtremaFinder
from extrema.data.DataPlotter import DataPlotter
from extrema.data.DataReader import DataReader
from extrema.data.SpeedCalculator import SpeedCalculator


class Interface:
    data_reader = DataReader()
    data_extrema_finder = None
    data_plotter = DataPlotter()
    speed_calculator = SpeedCalculator()

    item_type = 0

    distance = 1
    maxima_height = 0
    minima_height = 0
    prominence = 0
    start_time = 0
    end_time = 0
    precision = 0

    current_debug_plot = None
    current_plot = None

    def set__plot_title(self, title):
        self.data_plotter.set__title(title)

    def set__plot_y_axis(self, y_axis):
        self.data_plotter.set__y_axis(y_axis)

    def set__plot_x_axis(self, x_axis):
        self.data_plotter.set__x_axis(x_axis)

    def set__file_path(self, file_path):
        self.data_reader.__read_data__(file_path)

    def set__data_type(self, option):
        self.item_type = option

    def set__distance(self, distance):
        self.distance = distance

    def set__maxima_height(self, maxima_height):
        self.maxima_height = maxima_height

    def set__minima_height(self, minima_height):
        self.minima_height = minima_height

    def set__precision(self, precision):
        self.precision = precision

    def set__prominence(self, prominence):
        self.prominence = prominence

    def set__start_time(self, start_time):
        self.start_time = start_time

    def set__end_time(self, end_time):
        self.end_time = end_time

    def get__minima_extrema(self):
        self._set_extrema_options()

        return self.data_extrema_finder.find_minima()

    def get__data_list(self):
        return self.data_reader.get__data_list(self.item_type)

    def get__maxima_extrema(self):
        self._set_extrema_options()

        return self.data_extrema_finder.find_maxima()

    def get__available_data_types(self):
        return self.data_reader.get__available_item_types()

    def get__time_list(self):
        return self.data_reader.get__time_list()

    def get__current_debug_plot(self):
        return self.current_debug_plot

    def get__current_plot(self):
        return self.current_plot

    def get__speed_maxima(self):
        self.speed_calculator.set__time_list(self.data_reader.get__time_list())
        self.speed_calculator.set__maxima_list(self.data_extrema_finder.find_maxima())
        self.speed_calculator.set__minima_list(self.data_extrema_finder.find_minima())
        self.speed_calculator.set__precision(self.precision)

        return self.speed_calculator.calculate_speed_maxima()

    def get__speed_minima(self):
        self.speed_calculator.set__time_list(self.data_reader.get__time_list())
        self.speed_calculator.set__maxima_list(self.data_extrema_finder.find_maxima())
        self.speed_calculator.set__minima_list(self.data_extrema_finder.find_minima())
        self.speed_calculator.set__precision(self.precision)

        return self.speed_calculator.calculate_speed_minima()

    def create__debug_plot_image(self):
        self._set_extrema_options()

        self.data_plotter.set__minima_list(self.data_extrema_finder.find_minima())
        self.data_plotter.set__maxima_list(self.data_extrema_finder.find_maxima())
        self.current_debug_plot = self.data_plotter.debug_plot(
            self.data_reader.get__time_list(),
            self.data_reader.get__data_list(self.item_type),
            self.start_time,
            self.end_time
        )

    def create__plot_image(self):
        self.current_plot = self.data_plotter.plot(
            self.data_reader.get__time_list(),
            self.data_reader.get__data_list(self.item_type),
        )

    # self.dataList = dataList
    # self.time_list = time_list
    # self.distance = distance
    # self.minima_height = minima_height
    # self.maxima_height = maxima_height
    # self.prominence = prominence
    # self.start_time = start_time
    # self.end_time = end_time

    # self.dataList = dataList
    # self.time_list = time_list
    # self.distance = distance
    # self.minima_height = minima_height
    # self.maxima_height = maxima_height
    # self.prominence = prominence
    # self.start_time = start_time
    # self.end_time = end_time

    def _set_extrema_options(self):
        self.data_extrema_finder = DataExtremaFinder(
            self.data_reader.get__data_list(self.item_type),
            self.data_reader.get__time_list(),
            self.distance,
            self.maxima_height,
            self.minima_height,
            self.prominence,
            self.start_time,
            self.end_time
        )

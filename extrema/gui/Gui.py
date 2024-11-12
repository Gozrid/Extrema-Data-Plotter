from tkinter import *
from tkinter.ttk import *

from extrema.gui.DataType import DataType
from extrema.gui.DebugPlot import DebugPlot
from extrema.gui.GuiMenu import GuiMenu
from extrema.gui.Plot import Plot
from extrema.gui.PlotAction import PlotAction
from extrema.gui.PlotDataTable import PlotDataTable
from extrema.gui.PlotNaming import PlotNaming
from extrema.gui.VariableSettings import VariableSettings


class Gui:
    # Default values
    maxima_height = 0.0
    minima_height = 0.0
    prominence = 0
    n = 0
    start_time = 0.0
    end_time = 0.0
    precision = 0

    master = Tk()

    variable_settings = None
    gui_menu = None
    data_type = None
    plot_action = None
    debug_plot = None
    plot_data_table = None
    plot = None
    plot_naming = None

    interface = None

    def __init__(self, interface, maxima_height, minima_height, prominence, n, start_time, end_time, precision):
        self.interface = interface

        self.maxima_height = maxima_height
        self.minima_height = minima_height
        self.prominence = prominence
        self.n = n
        self.start_time = start_time
        self.end_time = end_time
        self.precision = precision

        self.gui_menu = GuiMenu(self.master, self.interface, self)

    def create(self):
        self.create_settings()
        self.create_data_type()
        self.create_plot_action()
        self.create_debug_plot()
        self.create_plot_data_table()
        self.create_plot()
        self.create_plot_naming()

        self.gui_menu.create()

        self.master.mainloop()

    def update_data_type(self):
        self.data_type.set__available_data_types(self.interface.get__available_data_types())

    def create_plot_naming(self):
        frame = Frame(self.master, relief="groove", borderwidth=1)
        frame.grid(row=2, column=0, sticky='wne')

        self.plot_naming = PlotNaming(frame, self.interface)
        self.plot_naming.create()

    def create_plot(self):
        frame = Frame(self.master, relief="flat", borderwidth=1)
        frame.grid(row=1, column=2, columnspan=2, rowspan=2, sticky='we')

        self.plot = Plot(frame, self.interface)
        self.plot.create()

    def create_plot_data_table(self):
        frame = Frame(self.master, relief="groove", borderwidth=1)
        frame.grid(row=0, column=3)

        self.plot_data_table = PlotDataTable(frame, self.interface)
        self.plot_data_table.create()

    def create_debug_plot(self):
        frame = Frame(self.master, relief="flat", borderwidth=1)
        frame.grid(row=0, column=2, sticky='we')

        self.debug_plot = DebugPlot(frame, self.interface)
        self.debug_plot.create()

    def create_plot_action(self):
        frame = Frame(self.master, relief="flat", borderwidth=0)
        frame.grid(row=3, column=0)

        self.plot_action = PlotAction(frame, self.interface, self)
        self.plot_action.create()

    def create_data_type(self):
        frame = Frame(self.master, relief="groove", borderwidth=1)
        frame.grid(row=1, column=0, sticky='wne')

        self.data_type = DataType(frame, self.interface)
        self.data_type.create(self.interface.get__available_data_types())

    def create_settings(self):
        frame = Frame(self.master, relief="groove", borderwidth=1)
        frame.grid(row=0, column=0)

        self.variable_settings = VariableSettings(self.interface, frame, self.maxima_height, self.minima_height,
                                                  self.prominence,
                                                  self.n,
                                                  self.start_time, self.end_time, self.precision)
        self.variable_settings.create()

    def update_plots(self):
        self.debug_plot.update()
        self.plot.update()
        self.plot_data_table.update()

    def _print_settings(self):
        print("maxima_height", self.variable_settings.get__maxima_height())
        print("minima_height", self.variable_settings.get__minima_height())
        print("prominence", self.variable_settings.get__prominence())
        print("n", self.variable_settings.get__n())
        print("start_time", self.variable_settings.get__start_time())
        print("end_time", self.variable_settings.get__end_time())

    def _print_data_types(self):
        print(self.interface.get__available_data_types())

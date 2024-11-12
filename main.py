from extrema.Interface import Interface
from extrema.gui.Gui import Gui

maxima_height = -4.5  # Minimum height for maxima (goes up)
minima_height = -6  # Minimum height for minima (goes down)
prominence = 4  # Prominence of extrema (vertical minimum distance between maxima and minima) -> filter out noise
n = 50  # number of points to be checked before and after extrema
start_time = 8.65  # The time from where extremas should be calculated
end_time = 20  # The time to where extremas should be calculated
precision = 2  # Precision of speed between extremas (decimals after .)

interface = Interface()

gui = Gui(interface, maxima_height, minima_height, prominence, n, start_time, end_time, precision)
gui.create()

from tkinter import Menu
from tkinter import filedialog as fd


class GuiMenu:
    master = None
    interface = None
    gui = None

    menu = None
    file_path = ''

    def __init__(self, master, interface, gui):
        self.master = master
        self.interface = interface
        self.gui = gui

    def create(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Example menu
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Open...', command=self._open_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.master.quit)

    def _open_file(self):
        self.interface.set__file_path(fd.askopenfilename(filetypes=[('MOT Files', '*.mot')], initialdir='.'))
        self.gui.update_data_type()

from tkinter import OptionMenu, StringVar, Button, Label


class DataType:
    interface = None
    master = None

    option_menu = None
    options = []
    selected_option = None

    def __init__(self, master, interface):
        self.interface = interface
        self.master = master

    def create(self, options):
        Label(self.master, text='Data column', font='bold').grid(row=0, column=0, sticky='w')

        self.selected_option = StringVar(None)
        self.options = options

        new_options = []
        for i in range(len(self.options)):
            if i > 0:
                new_options.append(self.options[i])

        new_preselected = ''

        if len(new_options) > 0:
            new_preselected = self.options[0]

        self.option_menu = OptionMenu(self.master, self.selected_option, new_preselected, *new_options)
        self.option_menu.grid(row=1, column=0)
        Button(self.master, text='Set', command=self.set_settings).grid(row=1, column=1)

    def set_settings(self):
        self.interface.set__data_type(self.selected_option.get())

    def set__available_data_types(self, options):
        # TOOD: Should delete all options to refresh the list
        print("updating...")
        self.options = options

        new_options = []
        menu = self.option_menu["menu"]
        menu.delete(0, "end")
        for i in range(len(self.options)):

            menu.add_command(label=self.options[i],
                             command=lambda value=self.options[i]: self.selected_option.set(value))

            if i > 0:
                new_options.append(self.options[i])

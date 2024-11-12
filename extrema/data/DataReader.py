import re

from extrema.entities.MovementData import Movement_Data


class DataReader:
    movement_data_list = []

    def __read_data__(self, file_name):
        regexp = re.compile(r'([-]?\d+[.]\d+\s+)+')

        f = open(file_name, "r")
        lines = f.readlines()
        f.close()

        if len(self.movement_data_list) > 0:
            self.movement_data_list.clear()

        for i in range(len(lines)):
            if regexp.search(lines[i]):
                items = ' '.join(lines[i].split()).replace(';', '').split(' ')
                self.movement_data_list.append(Movement_Data(
                    float(items[0]),
                    float(items[1]),
                    float(items[2]),
                    float(items[3]),
                    float(items[4]),
                    float(items[5]),
                    float(items[6]),
                    float(items[7]),
                    float(items[8]),
                    float(items[9]),
                    float(items[10]),
                    float(items[11]),
                    float(items[12]),
                    float(items[13]),
                    float(items[14]),
                    float(items[15]),
                    float(items[16]),
                    float(items[17]),
                    float(items[18]),
                    float(items[19]),
                    float(items[20]),
                    float(items[21]),
                    float(items[22]),
                    float(items[23]),
                    float(items[24]),
                    float(items[25]),
                    float(items[26]),
                    float(items[27]),
                    float(items[28]),
                    float(items[29]),
                    float(items[30]),
                    float(items[31]),
                    float(items[32]),
                    float(items[33])))

        return self.movement_data_list

    def get__time_list(self):
        time_list = []

        for i in range(len(self.movement_data_list)):
            time_list.append(self.movement_data_list[i].time)

        return time_list

    def get__available_item_types(self):
        if len(self.movement_data_list) == 0:
            return []
        return list(self.movement_data_list[0].get_as_dictionary().keys())

    def get__data_list(self, item_type):
        data_list = []

        for i in range(len(self.movement_data_list)):
            data_list.append(self.movement_data_list[i].get_as_dictionary()[item_type])

        return data_list

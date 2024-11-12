from scipy.signal import find_peaks


class DataExtremaFinder:
    dataList = []
    distance = 50
    maxima_height = -4.5
    minima_height = -6.
    prominence = 4
    start_time = 0
    end_time = 0

    minima_list = []
    maxima_list = []

    def __init__(self, dataList, time_list, distance, maxima_height, minima_height, prominence, start_time, end_time):
        self.dataList = dataList
        self.time_list = time_list
        self.distance = distance
        self.minima_height = minima_height
        self.maxima_height = maxima_height
        self.prominence = prominence
        self.start_time = start_time
        self.end_time = end_time

    def get__minima_list(self):
        if not self.minima_list:
            self.find_minima()

        return self.minima_list

    def get__maxima_list(self):
        if not self.maxima_list:
            self.find_maxima()

        return self.maxima_list

    def find_minima(self, data_list=None, time_list=None, distance=None, height=None, prominence=None, start_time=None,
                    end_time=None):
        local_height = height
        local_data_list = data_list

        if local_data_list is None:
            local_data_list = self.dataList

        if local_height is None:
            local_height = self.minima_height

        self.minima_list = self._find([-x for x in local_data_list], time_list, distance, -local_height, prominence,
                                      start_time, end_time)

        return self.minima_list

    def find_maxima(self, data_list=None, time_list=None, distance=None, height=None, prominence=None, start_time=None,
                    end_time=None):
        local_height = height

        if local_height is None:
            local_height = self.maxima_height

        self.maxima_list = self._find(data_list, time_list, distance, local_height, prominence, start_time, end_time)

        return self.maxima_list

    def _find(self, data_list, time_list, distance, height, prominence, start_time, end_time):
        local_data_list = data_list
        local_time_list = time_list
        local_distance = distance
        local_height = height
        local_prominence = prominence
        local_start_time = start_time
        local_end_time = end_time

        if local_data_list is None:
            local_data_list = self.dataList

        if local_time_list is None:
            local_time_list = self.time_list

        if local_distance is None:
            local_distance = self.distance

        if local_height is None:
            local_height = self.maxima_height

        if local_prominence is None:
            local_prominence = self.prominence

        if local_start_time is None:
            local_start_time = self.start_time

        if local_end_time is None:
            local_end_time = self.end_time

        found_peaks, _ = find_peaks(local_data_list, distance=local_distance, height=local_height,
                                    prominence=local_prominence)

        new_peaks = []

        for peak in found_peaks:
            if local_end_time != 0:
                if local_start_time < local_time_list[peak] < local_end_time:
                    new_peaks.append(peak)
            else:
                if local_time_list[peak] > local_start_time:
                    new_peaks.append(peak)

        return new_peaks

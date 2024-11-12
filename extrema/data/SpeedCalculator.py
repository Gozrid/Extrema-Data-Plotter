class SpeedCalculator:
    maxima_list = []
    minima_list = []
    time_list = []
    precision = 0

    def set__maxima_list(self, maxima_list):
        self.maxima_list = maxima_list

    def set__minima_list(self, minima_list):
        self.minima_list = minima_list

    def set__time_list(self, time_list):
        self.time_list = time_list

    def set__precision(self, precision):
        self.precision = precision

    def calculate_speed_maxima(self):
        return self._calculate(self.maxima_list)

    def calculate_speed_minima(self):
        return self._calculate(self.minima_list)

    def _calculate(self, extrema_list):
        speed = 0.0
        counts = 0
        for i in range(len(extrema_list)):
            if i > 0:
                speed += (
                        self.time_list[extrema_list[i - 1]] -
                        self.time_list[extrema_list[i]])
                counts += 1

        return round(abs(speed / counts), self.precision)

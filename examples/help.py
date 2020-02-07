import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.signal as sig


class Filter:
    def __init__(self):
        self.data = pd.read_fwf('../data/EXPORT01.TXT')
        x = self.data['_KM.M____']
        self.N = self.data.shape[0]
        self.x_axis = np.linspace(0, 1 / (x[1] - x[0]), self.N)

    def plot_wavelength(self, column):
        y = self.data[column]
        amplitude = np.fft.fft(y)
        plt.plot(self.N / 4 * self.x_axis[2:self.N // 2] ** (-1), np.abs(amplitude)[2:self.N // 2] / self.N)
        plt.xlabel('wavelength [m]')
        plt.ylabel('amplitude [mm]')
        plt.xscale('log')
        plt.grid(True, which='major')
        plt.grid(True, which='minor')
        plt.show()

    @staticmethod
    def filter_data():
        a = sig.cheb1ap(6, 3)
        plt.plot(a[1])
        plt.show()



# Filter().plot_wavelength('AlgPrR')
Filter.filter_data()
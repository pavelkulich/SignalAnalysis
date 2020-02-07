import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
import numpy as np


def import_file(directory, file):
    path = f'{directory}/{file}'
    data_frame = pd.read_fwf(path).dropna()
    return data_frame


def _butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [high, low], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = _butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def _butter_lowpass(lowcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = butter(order, low, btype='low')
    return b, a


def butter_lowpass_filter(data, lowcut, fs, order=5):
    b, a = _butter_lowpass(lowcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def _butter_highpass(highcut, fs, order=5):
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = butter(order, high, btype='high')
    return b, a


def butter_highpass_filter(data, highcut, fs, order=5):
    b, a = _butter_highpass(highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def plot_frequency(x, filtered, not_filtered, N):
    plt.plot(x[0:N // 2], np.abs(filtered)[0:N // 2] / N)
    plt.plot(x[0:N // 2], np.abs(not_filtered)[0:N // 2] / N)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('amplitude [mm]')
    plt.xscale('log')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.show()


def plot_wavelength(x, y, N):
    plt.bar(N * x[2:N // 2] ** (-1), np.abs(y)[2:N // 2] / N)
    plt.xlabel('wavelength [m]')
    plt.ylabel('amplitude [mm]')
    plt.xscale('log')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.savefig('plots/dft.png')
    plt.show()


def main():
    # data import - you need to set propper arguments in import_file function
    data = import_file("data", "EXPORT01.txt")
    magnitude = data["AlgPrL"]
    x = data['_KM.M____']

    # input data
    fs = 1000
    low_f = 333
    high_f = 40
    ############

    # low pass filter for non filtered data
    filtered_data_low = butter_lowpass_filter(magnitude, low_f, fs, 5)

    # high pass filter for non filtered data
    filtered_data_high = butter_highpass_filter(magnitude, high_f, fs, 5)

    # high pass filter for non filtered data
    filtered_data_band = butter_bandpass_filter(magnitude, low_f, high_f, fs, 5)

    # plot all
    plt.plot(x, magnitude)
    plt.plot(x, filtered_data_low)
    plt.plot(x, filtered_data_high)
    plt.plot(x, filtered_data_band)
    plt.legend(('original', 'lowpass', 'highpass', 'bandpass'))
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.show()

    # fft calculation
    amp = np.fft.fft(magnitude)
    amp_band = np.fft.fft(filtered_data_high)

    # plot
    N = len(magnitude)
    T = x[1] - x[0]
    f = np.linspace(0, 1 / T, N)
    plot_frequency(f, amp_band, amp, N)
    plot_wavelength(f, amp_band, N)


if __name__ == '__main__':
    main()

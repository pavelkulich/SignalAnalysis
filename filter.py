import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, sosfilt
import numpy as np


def import_file(directory, file):
    path = f'{directory}/{file}'
    data_frame = pd.read_fwf(path).dropna().reset_index()
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


def butter_filter_plot():
    # b, a = _butter_lowpass(40, 1000, 5)
    # # b, a = butter(4, 40, 'low', analog=True)
    # w, h = freqs(b, a)
    # plt.semilogx(w, 20 * np.log10(abs(h)))
    # plt.title('Butterworth filter frequency response')
    # plt.xlabel('Frequency [radians / second]')
    # plt.ylabel('Amplitude [dB]')
    # plt.margins(0, 0.1)
    # plt.grid(which='both', axis='both')
    # plt.axvline(40, color='green')  # cutoff frequency
    # plt.show()
    pass


def sos_butter_lowpass(data, lowcut, fs, order=10):
    sos = butter(order, lowcut, 'lp', fs=fs, output='sos')
    filtered = sosfilt(sos, data)
    return filtered


def sos_butter_highpass(data, highcut, fs, order=10):
    sos = butter(order, highcut, 'hp', fs=fs, output='sos')
    filtered = sosfilt(sos, data)
    return filtered


def sos_butter_bandpass(data, highcut, lowcut, fs, order=10):
    sos = butter(order, [highcut, lowcut], 'bp', fs=fs, output='sos')
    filtered = sosfilt(sos, data)
    return filtered


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
    plt.plot(N * x[2:N // 2] ** (-1), np.abs(y)[2:N // 2] / N)
    plt.xlabel('wavelength [m]')
    plt.ylabel('amplitude [mm]')
    plt.xscale('log')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.savefig('plots/dft.png')
    plt.show()

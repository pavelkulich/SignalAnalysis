import numpy as np
import matplotlib.pyplot as plt
import database_manager as dbm


def dft(x):
    """
    Compute the discrete Fourier Transform of the 1D array x
    :param x: (array)
    """

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)


def plot_frequency(x, y, N):
    plt.plot(x[0:N // 2] ** (-1), np.abs(y)[0:N // 2] / N)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('amplitude [mm]')
    plt.xscale('log')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.show()


def plot_wavelength(x, y, N):
    plt.plot(N / 4 * x[2:N // 2] ** (-1), np.abs(y)[2:N // 2] / N)
    plt.xlabel('wavelength [m]')
    plt.ylabel('amplitude [mm]')
    plt.xscale('log')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.savefig('plots/dft.png')
    plt.show()


def main():
    plot = ('MV_2015_03_15', 106.000, 107.000, 'VK_D2')
    database = dbm.DbManager('signal.sqlite3')
    data = database.fetch_data(plot[0], plot[1], plot[2], plot[3])
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    # amp = dft(y)
    amp = np.fft.fft(y)
    T = x[1] - x[0]
    N = len(y)
    f = np.linspace(0, 1 / T, N)
    plot_wavelength(f, amp, N)

main()
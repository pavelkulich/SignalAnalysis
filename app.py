import matplotlib.pyplot as plt
import database_manager as dbm


def plot_data(data, param):
    plt.figure(figsize=(12, 8))
    plt.plot(data[0], data[1])
    plt.title(param)
    plt.legend(param.replace(' ', '').split(','))
    plt.xlabel('stationing [km]')
    plt.ylabel('amplitude [mm]')
    plt.grid(True)
    plt.savefig(f'plots/{param}_from_{min(data[0])}_to_{max(data[0])}.png')
    plt.close()
    # plt.show()


def main():
    database = dbm.DbManager()

    plots = [('MV_2015_03_15', 105.000, 105.100, 'VL_D1, VP_D1'),
             ('MV_2015_03_15', 106.000, 106.100, 'VP_D1'),
             ('MV_2015_03_15', 107.000, 107.100, 'VK_D2')]

    for plot in plots:
        data = database.fetch_data(plot[0], plot[1], plot[2], plot[3])
        x = [row[0] for row in data]
        y = [row[1:] for row in data]
        data_frame = [x, y]
        plot_data(data_frame, plot[3])

    database.disconnect()


main()

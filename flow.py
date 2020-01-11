import pandas as pd
import matplotlib.pyplot as plt


# step 1
def import_file(path):
    data_frame = pd.read_fwf(path)
    table_head = data_frame.columns.values
    return data_frame, table_head


def plot_data(data_frame):
    plt.plot(data_frame['_KM.M____'], data_frame['VL_D1'])
    plt.plot(data_frame['_KM.M____'], data_frame['VP_D1'])
    plt.title('Vyska D1')
    plt.ylabel('[mm]')
    plt.show()

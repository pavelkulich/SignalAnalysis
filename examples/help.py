import matplotlib.pyplot as plt
import pandas as pd
import spectrum as sp
import database_manager as dbm
import os


# def import_file(path):
#     data_frame = pd.read_fwf(path)
#     table_head = data_frame.columns.values
#     return data_frame, table_head

def import_file(directory, file):
    path = f'{directory}/{file}'
    data_frame = pd.read_fwf(path)
    table_head = data_frame.columns.values
    plot_data(data_frame)
    return data_frame


def plot_data(data_frame):
    # plt.figure(figsize=(20, 12))
    plt.plot(data_frame['_KM.M____'], data_frame['TOP_PRL'])
    plt.plot(data_frame['_KM.M____'], data_frame['TOP_PRR'])
    plt.xlabel('staničení [km]')
    plt.ylabel('amplituda [mm]')
    plt.grid(True, which='major')
    plt.grid(True, which='minor')
    plt.savefig('primary.png')


# data = import_file("../data", "EXPORT00.txt")
# sp.plot_frequency(data['_KM.M____'], data['TOP_PRL'], data.size)
# plot_data(data)

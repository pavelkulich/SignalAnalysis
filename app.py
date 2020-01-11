import matplotlib.pyplot as plt
import pandas as pd
import database_manager as dbm
import os


def import_file(directory, file):
    path = f'{directory}/{file}'
    data_frame = pd.read_fwf(path)
    table_head = data_frame.columns.values
    plot_data(data_frame)
    # return data_frame, table_head


def plot_data(data_frame):
    plt.plot(data_frame['_KM.M____'], data_frame['VL_D1'])
    plt.plot(data_frame['_KM.M____'], data_frame['VP_D1'])
    plt.title('Vyska D1')
    plt.ylabel('[mm]')
    plt.show()


def read_all_files(directory):
    directory_list = os.listdir(directory)
    for file in directory_list:
        import_file(directory, file)


read_all_files('data')








# # /////////////////
# #  block to import data a save into db
# data, head = import_file("data/2015_03_15.txt")
#
# # data_list = [item for item in data.values]
# data_list = []
# for item in data.values:
#     data_list.append(item)
#
# db_path = "signal.sqlite3"
# database = dbm.DbManager(db_path)
# database.create_table("MV_data")
# database.insert_data("MV_data", data_list)
# database.disconnect()
# # /////////////////

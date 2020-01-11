import matplotlib as plt
import pandas as pd
import database_manager as dbm
import os


def import_file(directory, file):
    path = f'{directory}/{file}'
    data_frame = pd.read_fwf(path)
    # table_head = data_frame.columns.values
    # plot_data(data_frame)
    return data_frame


# #  slouzi pro kontrolu spravnosti importu
# def plot_data(data_frame):
#     plt.plot(data_frame['_KM.M____'], data_frame['VL_D1'])
#     plt.plot(data_frame['_KM.M____'], data_frame['VP_D1'])
#     plt.title('Vyska D1')
#     plt.ylabel('[mm]')
#     plt.show()


def main(directory, ):
    database = dbm.DbManager()

    directory_list = os.listdir(directory)
    for file in directory_list:
        data_frame = import_file(directory, file)
        data_list = [item for item in data_frame.values]
        db_table = f'MV_{file.split(sep=".")[0]}'  # https://www.w3schools.com/python/ref_string_split.asp

        if database.create_table(db_table):
            database.insert_data(db_table, data_list)

    database.disconnect()

# main('data')

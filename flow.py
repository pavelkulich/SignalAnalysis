# import pandas as pd
# import matplotlib.pyplot as plt
# import os
# import database_manager as dbm
#
#
# # step 1
# def import_file(path):
#     data_frame = pd.read_fwf(path)
#     table_head = data_frame.columns.values
#     return data_frame, table_head
#
#
# def plot_data(data_frame):
#     plt.plot(data_frame['_KM.M____'], data_frame['VL_D1'])
#     plt.plot(data_frame['_KM.M____'], data_frame['VP_D1'])
#     plt.title('Vyska D1')
#     plt.ylabel('[mm]')
#     plt.show()
#
# # step 2
#
# def import_file2(directory, file):
#     path = f'{directory}/{file}'
#     data_frame = pd.read_fwf(path)
#     # table_head = data_frame.columns.values
#     # plot_data(data_frame)
#     return data_frame
#
# def read_all_files(directory):
#     directory_list = os.listdir(directory)
#     return directory_list
#
#
# def run_importer(directory, db_path):
#     database = dbm.DbManager(db_path)
#
#     directory_list = read_all_files(directory)
#     for file in directory_list:
#         # print(file)
#         data_frame = import_file(directory, file)
#         data_list = [item for item in data_frame.values]
#         db_table = f'MV_{file.split(sep=".")[0]}'  # https://www.w3schools.com/python/ref_string_split.asp
#
#         database.create_table(db_table)
#         database.insert_data(db_table, data_list)
#
#     database.disconnect()
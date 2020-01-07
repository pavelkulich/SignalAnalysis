import matplotlib.pyplot as plt
import pandas as pd
import database_manager as dbm


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


data, head = import_file("data/2015_03_15.txt")

db_path = "sqlite:///signal.sqlite3"
database = dbm.DbManager(db_path)
table = database.create_table("MV_data")
print(type(table))
# table.insert(data)
# plot_data(data)



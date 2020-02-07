import sqlite3


class DbManager:
    def __init__(self, db_path='signal.sqlite3'):
        self._db_path = db_path
        try:
            self._sqliteConnection = sqlite3.connect(self._db_path)
            self._cursor = self._sqliteConnection.cursor()
            print(f"Connected to SQLite {self._sqliteConnection}")

        except sqlite3.Error as error:
            print("Failed to connect sqlite table", error)

        # self.engine = db.create_engine(file_path, echo=True)
        # self.connection = self.engine.connect()
        # self.meta = db.MetaData()

    def disconnect(self):
        self._sqliteConnection.close()
        print('DB disconnected')

    def create_table(self, table_name):
        try:
            query = f"""CREATE TABLE {table_name} (
                        "km"	    REAL NOT NULL,
                        "RK_1_INF"	REAL NOT NULL,
                        "RYCH"  	REAL NOT NULL,
                        "SL_D1" 	REAL NOT NULL,
                        "SP_D1" 	REAL NOT NULL,
                        "SK_D2" 	REAL NOT NULL,
                        "K_70_INF" 	REAL NOT NULL,
                        "PK_CEL" 	REAL NOT NULL,
                        "ZKS_P" 	REAL NOT NULL,
                        "ZKS_B" 	REAL NOT NULL,
                        "VK_D2" 	REAL NOT NULL,
                        "VL_D1" 	REAL NOT NULL,
                        "VP_D1" 	REAL NOT NULL
                        );"""

            self._cursor.execute(query)
            print(f'Table {table_name} has been created')
            return True
        except sqlite3.Error as error:
            print(error)
            return False

    def insert_data(self, table_name, data):
        try:
            query = f'INSERT INTO {table_name} (km, RK_1_INF, RYCH, SL_D1, SP_D1, SK_D2, K_70_INF, PK_CEL, ZKS_P, ZKS_B, VK_D2, VL_D1, VP_D1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self._cursor.executemany(query, data)
            self._sqliteConnection.commit()
            print(f'{len(data)} rows has been inserted into {table_name}')
        except Exception as e:
            print(e)

    def fetch_data(self, table_name, from_km, to_km, parameter):
        query = f'SELECT km,{parameter} FROM {table_name} WHERE km BETWEEN {from_km} AND {to_km}'
        self._cursor.execute(query)
        data = self._cursor.fetchall()
        return data

    def find_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
        self._cursor.execute(query)
        tables = self._cursor.fetchall()
        return tables

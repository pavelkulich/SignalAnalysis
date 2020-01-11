import sqlalchemy as db
import sqlite3


class DbManager:
    def __init__(self, db_path):
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
        except sqlite3.Error as error:
            print(error)

    def insert_data(self, table_name, data):
        query = f'INSERT INTO {table_name} (km, RK_1_INF, RYCH, SL_D1, SP_D1, SK_D2, K_70_INF, PK_CEL, ZKS_P, ZKS_B, VK_D2, VL_D1, VP_D1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self._cursor.executemany(query, data)
        # self._sqliteConnection.commit()

    def create_table_alchemy(self, table_name):
        try:
            table = db.Table(table_name, self.meta, db.Column('km', db.Float),
                             db.Column('RK_1-INF', db.Float), db.Column('RYCH', db.Float), db.Column('SL_D1', db.Float),
                             db.Column('SP_D1', db.Float), db.Column('SK_D2', db.Float),
                             db.Column('K_70-INF', db.Float),
                             db.Column('PK_CEL', db.Float), db.Column('ZKS_%', db.Float), db.Column('ZKS_B', db.Float),
                             db.Column('VK_D2', db.Float), db.Column('VL_D1', db.Float), db.Column('VP_D1', db.Float))
            self.meta.create_all(self.engine)
            return table
        except Exception as e:
            print(e)

import sqlalchemy as db


class DbManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.engine = db.create_engine(file_path, echo=True)
        self.connection = self.engine.connect()
        self.meta = db.MetaData()

    def create_table(self, table_name):
        try:
            table = db.Table(table_name, self.meta, db.Column('id', db.Integer, primary_key=True), db.Column('km', db.Float),
                     db.Column('RK_1-INF', db.Float), db.Column('RYCH', db.Float), db.Column('SL_D1', db.Float),
                     db.Column('SP_D1', db.Float), db.Column('SK_D2', db.Float), db.Column('K_70-INF', db.Float),
                     db.Column('PK_CEL', db.Float), db.Column('ZKS_%', db.Float), db.Column('ZKS_B', db.Float),
                     db.Column('VK_D2', db.Float), db.Column('VL_D1', db.Float), db.Column('VP_D1', db.Float))
            self.meta.create_all(self.engine)
            return table
        except Exception as e:
            print(e)

#    db.Column('name', db.String),)
#
# students = db.Table(
#    'students', meta,
#    db.Column('id', db.Integer, primary_key = True),
#    db.Column('name', db.String),
#    db.Column('lastname', db.String),
# )
# meta.create_all(engine)
# meta.create_all(engine)

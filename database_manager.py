import sqlalchemy as db

engine = db.create_engine("sqlite:///signal.sqlite3", echo=True)
connection = engine.connect()

# meta = db.MetaData()
#
# students = db.Table(
#    'students', meta,
#    db.Column('id', db.Integer, primary_key = True),
#    db.Column('name', db.String),
#    db.Column('lastname', db.String),
# )
# meta.create_all(engine)
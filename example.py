from sqlalchemy import text, MetaData, Table, Column, Integer, String

from db import tables
from db.session import engine, session_scope


text_sql = text("select * from cars_db.cars")
with session_scope() as session:
    for i in session.execute(text_sql).fetchall():
        print(i)


with session_scope() as session:
    for i in session.query(tables.Brand).from_statement(text(
        "select * from cars_db.brands"
    )).all():
        print(i)


metadata = MetaData()
brands = Table(
    'brands',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(100), nullable=False),
    Column('country', String(100), nullable=False)
)
metadata.create_all(engine)


with session_scope() as session:
    for i in session.execute(brands.select().where(brands.c.id == 1)).fetchall():
        print(i)

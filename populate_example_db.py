import sqlalchemy

from config import Config

engine = sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI)
with engine.connect() as connection:
    connection.execute(sqlalchemy.text("insert into example_table (bigger_id, description, is_entry, freeflow) values (1234567890, 'This is a description', true, 'Lots of text here');"))
    connection.execute(sqlalchemy.text("insert into example_table (bigger_id, description, is_entry, freeflow) values (1234567899, 'This is a different description', false, 'There really isn not any text here at all');"))
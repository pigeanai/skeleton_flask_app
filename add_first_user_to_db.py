import sqlalchemy

from config import Config

# Add a test user with username 'user' and password 'password'
engine = sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI)
with engine.begin() as connection:
    connection.execute(sqlalchemy.text("insert into users (username, email, password_hash) values ('user', 'user@example.com', 'scrypt:32768:8:1$CPg09dJWjuKfVcGH$1d8660d101974f9e4143ae0f3ced0fd22ed479a740625a3b75e89d8da12f3f32b792794ace2ab2f9cc8d0bb65a4b59fc5c09f36861344e8e477ec356720d641d');"))
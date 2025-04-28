# skeleton_flask_app

The purpose of this app is to act as a base to fork and create other projects from. It sets up a reasonable project structure and has the basic implementation of fairly common web application elements, such as a connecting to a database, adding-to/removing-from/querying that database, and handling migrations. It sets up blueprints to allow the routes to be developed neatly. Authentication is handled in logging in, logging out, and restricting access to certain pages. There is also a Dockerfile to allow easy creation of docker images.

Error handling is non existent, tests even less so. This application lets you log in, add and/or delete users, and log out; hardly an application to be deployed anywhere. In fact, some of this functionality is purely to act as examples of add/deleting/querying data using SQLAlchemy ORM.

This uses [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) to manage db migrations. To summarise the useage:

Set up the project to use flask-migrate (this has already been done):
```bash
flask db init
```

Create a new migration:
```bash
flask db migrate -m "description here"
```

Apply migrations:
```bash
flask db upgrade
```

Much of this project is heavily inspired by [Miguel Grinberg's Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) which I first found circa 2015-2016 and has been an invaluable reference ever since.

By the way, if you are reading this and aren't future me, I'm shocked - this is a project created for my own consumption, but I have made it public on the off-chance someone else comes across it and may find any of it useful. Also, in case I somehow manage to lose my GitHub credentials it'll be handy to be able to clone this on a new account.

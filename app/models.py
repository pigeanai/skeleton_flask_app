from app import db

class ExampleTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
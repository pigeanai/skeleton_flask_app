from app import db

class ExampleTable(db.Model):
    __tablename__ = "example_table"
    
    id = db.Column(db.Integer, primary_key=True)
    bigger_id = db.Column(db.BigInteger)
    description = db.Column(db.String(255))
    is_entry = db.Column(db.Boolean)
    freeflow = db.Column(db.Text)
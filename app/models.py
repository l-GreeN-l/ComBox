from app import db
from datetime import datetime
from app import db

class Command(db.Model):
    id = db.Column(db.String(100),  primary_key=True)   # ИД привязанный к команде и вязывающий ее с формой
    name = db.Column(db.String(100))
    command = db.Column(db.String(1000))

    def __repr__(self):
        return '<Command {}>'.format(self.name)
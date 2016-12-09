from app import db

class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(32))

    password = db.Column(db.String(64), default='#')

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            password=self.password
        )
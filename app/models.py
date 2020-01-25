from app import db


class PLZ(db.Model):
    __tablename__ = "plz"
    id = db.Column("id", db.Integer(), primary_key=True)
    plz = db.Column("plz", db.Integer())
    long = db.Column("lang", db.Float())
    lat = db.Column("lat", db.Float())

    def __repr__(self):
        return f"<PLZ {self.plz}>"

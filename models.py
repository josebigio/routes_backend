from app import db
from sqlalchemy.dialects.postgresql import JSON


class stops(db.Model):
    __tablename__ = 'GTFS_STOPS'

    stop_id = db.Column(db.Integer, primary_key=True)
    stop_code = db.Column(db.String())
    stop_name = db.Column(db.String())
    stop_desc = db.Column(db.String())
    stop_lat = db.Column(db.Float())
    stop_lon = db.Column(db.Float())
    zone_id = db.Column(db.Float())
    stop_url = db.Column(db.Float())
    location_type = db.Column(db.Integer)
    parent_station = db.Column(db.Integer)
    stop_timezone = db.Column(db.String())
    wheelchair_boarding = db.Column(db.Boolean)

    def __repr__(self):
        return '<id {}>'.format(self.stop_id)
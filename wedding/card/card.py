from .. import db
from sqlalchemy import event
import datetime

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    message = db.Column(db.String(255), nullable = False)
    image = db.Column(db.String(120))
    status = db.Column(db.Integer, nullable = False, default = 0)
    created_at = db.Column(db.DateTime, nullable = False, server_default = db.func.current_timestamp())

    def __repr__(self):
        return '<Cards %r>' % self.name

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'message': self.message, 'image': self.image, 'created_at': self.created_at.timestamp()}


@event.listens_for(Cards, 'before_insert')
def update_time(mapper, connect, target):
    target.created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

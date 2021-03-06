from extensions import db
from models.BaseModel import BaseModel

class CHANNEL:
    SMS = 'sms'
    PUSHNOTIFICATION = 'push notification'
    EMAIL = 'email'

class TYPE:
    SINGLE = 'single'
    GROUP = 'group'

class Notification(BaseModel):
    def __repr__(self):
        return f"<Notification> id:{self.id}, message: {self.message}"

    __tablename__ = "notifications"

    channel = db.Column(db.String(30), index=True, nullable=True)
    type = db.Column(db.String(30), index=True, nullable=False)
    group_name = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), index=True, nullable=False)
    message = db.Column(db.Text)
    status = db.Column(db.String(30), nullable=True)
    user = db.relationship('User', lazy=True)

    def format(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'channel': self.channel,
            'type': self.type,
            'group_name': self.group_name,
            'user': self.user.format(),
            'message': self.message,
            'status': self.status
        }
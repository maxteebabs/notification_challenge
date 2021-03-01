from .exceptions import db
from .models import BaseModel
from .models import Customer

class Channel:
    SMS = 'sms'
    Push_Notification = 'push notification'

class Type:
    Single = 'single'
    Group = 'group'

class Notification(BaseModel):
    channel = db.Column(db.String(30), index=True, nullable=True)
    type = db.Column(db.String(30), index=True, nullable=False)
    group_name = db.Column(db.String(30), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        Customer.id
    ), index=True, nullable=False)
    message = db.Column(db.Text)
from .models import BaseModel


class Type:
    SMS = 'sms'
    Email = 'email'


class Log(BaseModel):
    type = db.Column(db.String(30))
    customer_id = db.Column(db.Integer, nullable=True)
    response = db.Column(db.Text, nullable=True)
    request = db.Column(db.request, nullable=True)
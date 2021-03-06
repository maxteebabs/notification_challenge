from models.BaseModel import BaseModel
from extensions import db

class TYPE:
    CUSTOMER = 'customer'
    RIDER = 'rider'

class User(BaseModel):
    def __repr__(self):
        return f"<User> id:{self.id}, name: {self.name}"

    __tablename__ = "users"
    name = db.Column(db.String(70))
    mobile = db.Column(db.String(30))
    type = db.Column(db.String(30))
    language = db.Column(db.String(30), default='en')

    def format(self):
        return {
            'id': self.id,
            'name':self.name,
            'mobile': self.mobile,
            'language':self.language
        }

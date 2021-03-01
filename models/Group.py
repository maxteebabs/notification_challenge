from .extensions import db
from .models import BaseModel
from .models import Customer

class Group(BaseModel):
    name = db.Column(db.String(30))


class UserGroup(BaseModel):
    __tablename__ = "users_groups"
    group_id = db.Column(db.Integer, db.ForeignKey(Group.id))
    customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id))

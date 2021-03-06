from extensions import db
from models.BaseModel import BaseModel

class Group(BaseModel):
    def __repr__(self):
        return f"<Group> id:{self.id}, name: {self.name}"

    __tablename__ = "groups"
    name = db.Column(db.String(30))


class UserGroup(BaseModel):
    def __repr__(self):
        return f"<UserGroup> id:{self.id}, group: \
            {self.group_id}, user:{self.user_id}"

    __tablename__ = "users_groups"
    group_id = db.Column(db.Integer, db.ForeignKey(
        "groups.id"), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), index=True, nullable=False)
    user = db.relationship('User', lazy=True)   

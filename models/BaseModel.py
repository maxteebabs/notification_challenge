import sys
from .extensions import db

class BaseModel(db.Model):
    """Base table schema for all models to inherit from"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db_now())
    modified_at = db.Column(db.DateTime, default=db_now(), onupdate=db_now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    def save(self):
        try:
            db.session.add(self)
            db.commit()
        except:
            print(sys.exc_info())
            db.session.rollback()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()

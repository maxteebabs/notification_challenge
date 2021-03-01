from .models import BaseModel

class Customer(BaseModel):
    def __repr__(self):
        return f"<Customer> id:{self.id}, name: {self.name}"
        name = db.Column(db.String(70))
        mobile = db.Column(db.String(30))
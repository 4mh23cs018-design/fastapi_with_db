from models import User
from sqlalchemy.orm import session

class userRepo:
    def __init__(self,db:session):
        self.db = db

    def create_user(self,user:User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
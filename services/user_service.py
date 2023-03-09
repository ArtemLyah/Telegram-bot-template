from databases.models.user import User
from loader import db_session

class UserService():
    def addUser(self, telegram_id, name, username):
        user = User(telegram_id=telegram_id, name=name, username=username)
        db_session.add(user)
        db_session.commit()
    
    def getAllUser(self, telegram_id):
        return db_session.query(User).filter(User.telegram_id == telegram_id).one()
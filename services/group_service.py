from databases.models.group import Group
from loader import db_session

class GroupService():
    def addGroup(self, telegram_id, name, group_type):
        group = Group(telegram_id=telegram_id, name=name, type=group_type)
        db_session.add(group)
        db_session.commit()
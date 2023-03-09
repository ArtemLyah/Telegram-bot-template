from sqlalchemy.orm import relationship
from databases.models.user import User
from databases.models.group import Group
from loader import Database
import sqlalchemy as sa

class UserGroup(Database.Base):
    __tablename__ = "userGroup"
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    group_id = sa.Column(sa.Integer, sa.ForeignKey("group.id"))
    user = relationship("User", back_populates="userGroup")
    group = relationship("Group", back_populates="userGroup")

User.userGroup = relationship("UserGroup", order_by=UserGroup.id, back_populates="user")
Group.userGroup = relationship("UserGroup", order_by=UserGroup.id, back_populates="group")
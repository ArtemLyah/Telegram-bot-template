from databases.connection import Database
from aiogram.enums.chat_type import ChatType
import sqlalchemy as sa

class Group(Database.Base):
    __tablename__ = "group"
    id = sa.Column(sa.Integer, primary_key=True)
    telegram_id = sa.Column(sa.Text)
    name = sa.Column(sa.String)
    type = sa.Column(sa.Enum(ChatType))

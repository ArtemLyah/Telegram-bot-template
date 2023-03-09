from loader import Database
import sqlalchemy as sa

class User(Database.Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    telegram_id = sa.Column(sa.Text)
    name = sa.Column(sa.String)
    username = sa.Column(sa.String)
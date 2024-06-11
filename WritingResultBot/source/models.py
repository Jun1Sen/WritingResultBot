from sqlalchemy.orm import Mapped, mapped_column

from DB import Base, str_50
from sqlalchemy import MetaData, ForeignKey, CheckConstraint

metadata = MetaData()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key = True)
    telegramId: Mapped[int]
    FirstName: Mapped[str | None]
    SecondName: Mapped[str | None]

class ResultEGE(Base):
    __tablename__ = 'result_ege'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    subject: Mapped[str]
    result: Mapped[int] = mapped_column(CheckConstraint('result > 0'))



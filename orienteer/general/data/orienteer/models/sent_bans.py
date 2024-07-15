from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .common import Base


class SentBan(Base):
    __tablename__ = 'SentBan'

    id = Column(Integer, primary_key=True)
    last_sent_ban_id = Column(Integer)
    last_sent_roleban_id = Column(Integer)

from sqlalchemy import Column, DateTime, BigInteger, Text, UUID
from sqlalchemy.sql import func

from .common import Base


class DiscordAuth(Base):
    __tablename__ = 'discord_auth'

    user_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    discord_user_id = Column(BigInteger, nullable=False, unique=True)
    discord_username = Column(Text, nullable=False, unique=True)
    email = Column(Text)

    created_at = Column(DateTime, server_default=func.now())

    def __init__(self, user_id, discord_user_id, discord_username, email=None):
        self.user_id = user_id
        self.discord_user_id = discord_user_id
        self.discord_username = discord_username
        self.email = email

    def __repr__(self):
        return (f"<DiscordAuth(user_id='{self.user_id}', discord_user_id={self.discord_user_id}, "
                f"discord_username='{self.discord_username}', email='{self.email}')>")
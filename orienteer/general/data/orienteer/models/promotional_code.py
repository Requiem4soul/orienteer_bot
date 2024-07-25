from sqlalchemy import Column, JSON, Integer, DateTime, String, Boolean

from .common import Base


class PromotionalCode(Base):
    __tablename__ = 'promotional_codes'

    code = Column(String, nullable=False, primary_key=True)
    usages = Column(Integer, nullable=False, default=10000)
    jobs = Column(JSON, nullable=False, default={})
    dependencies = Column(JSON, nullable=False, default={})
    expiration_date = Column(DateTime, nullable=True)
    is_creator = Column(Boolean, nullable=False, default=False)

    def __init__(self, code, usages=None, jobs=None, dependencies=None, expiration_date=None, is_creator=None):
        self.code = code
        self.usages = usages
        self.jobs = jobs
        self.dependencies = dependencies
        self.expiration_date = expiration_date
        self.is_creator = is_creator

    def __repr__(self):
        return f"<PromotionalCodes(code='{self.code}', usages={self.usages}, jobs={self.jobs}, dependencies={self.dependencies}, expiration_date={self.expiration_date}, is_creator={self.is_creator})>"

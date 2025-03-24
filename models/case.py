from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)  # Keep this for auto-incrementing
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default="Open")
    lawyer_id = Column(Integer, ForeignKey('lawyers.id'), nullable=True)

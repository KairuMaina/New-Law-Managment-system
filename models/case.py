from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default="Open")
    lawyer_id = Column(Integer, ForeignKey('lawyers.id'))  # Foreign Key

    # Relationship
    lawyer = relationship("Lawyer", back_populates="cases")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Lawyer(Base):
    __tablename__ = "lawyers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String)

    cases = relationship("Case", back_populates="lawyer")

    def __repr__(self):
        return f"<Lawyer(name={self.name}, specialization={self.specialization})>"

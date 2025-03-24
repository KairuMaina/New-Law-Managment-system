from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Ensure this is correctly imported

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="Open")
    lawyer_id = Column(Integer, ForeignKey("lawyers.id"), nullable=True)

    lawyer = relationship("Lawyer", back_populates="cases")

    def __repr__(self):
        return f"<Case(title={self.title}, status={self.status})>"

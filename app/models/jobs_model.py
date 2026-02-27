from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class JobOffer(Base):
    __tablename__ = "job_offers"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False)
    skills_extracted = Column(Text, nullable=False)  
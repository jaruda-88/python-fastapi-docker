from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from databases.handler import Base


class BBS(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
"""Core models."""
import enum
from sqlalchemy import Column, TEXT, TIMESTAMP, ForeignKey, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer, TypeDecorator
from sqlalchemy.orm import relationship, backref

DBase = declarative_base()

class Base(DBase):
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False)

    def json(self) -> dict:
        """Class fields to JSON method."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class User(Base):
    __tablename__ = "users"
    name = Column(TEXT, nullable=False)

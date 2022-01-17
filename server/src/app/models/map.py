"""Core models."""
from ast import For
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
    games = relationship("Game")

class Game(Base):
    __tablename__ = "games"
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    units = relationship("Unit")
    buildings = relationship("Building")
    max_players = Column(Integer, nullable=False, default=1)

class Unit(Base):
    __tablename__ = "units"
    game_id = Column(Integer, ForeignKey('games.id', ondelete="CASCADE"))
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    parameters = relationship("UnitParameters")

class Building(Base):
    __tablename__ = "buildings"
    game_id = Column(Integer, ForeignKey('games.id', ondelete="CASCADE"))
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    parameters = relationship("BuildingParameters")

class UnitParameters(Base):
    __tablename__ = "unit_parameters"
    unit_id = Column(Integer, ForeignKey('units.id', ondelete="CASCADE"))
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    value = Column(TEXT, nullable=False)

class BuildingParameters(Base):
    __tablename__ = "building_parameters"
    building_id = Column(Integer, ForeignKey('buildings.id', ondelete="CASCADE"))
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    value = Column(TEXT, nullable=False)

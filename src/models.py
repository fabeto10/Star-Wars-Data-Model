import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorite = relationship("Favorite", back_populates="parent")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = relationship("user", back_populates="children")
    planet_id = Column(Integer, ForeignKey("user.id"))
    planet = relationship("favorite", back_populates="children")
    character_id = Column(Integer, ForeignKey("user.id"))
    character = relationship("favorite", back_populates="children")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship("favorite", back_populates="children")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship("favorite", back_populates="children")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
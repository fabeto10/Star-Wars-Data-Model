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

class Favorite(Base):
    __tablename__ = 'favorite'
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, ForeignKey("user.id"))
    user =Column(String(250), nullable=False)
    favorite = relationship("planet", backref="favorite")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, ForeignKey("user.id"))
    user= Column(String(250), nullable=False)
    favorite = relationship("character", backref="favorite")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
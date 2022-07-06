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
    favorite_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = relationship("User", back_populates="favorites")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("favorite", back_populates="children")
    planets = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates="favorites")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    favorites = relationship("Favorite", back_populates="planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable= False)
    gender = Column(String(250), nullable=False)
    favorites = relationship("Favorite", back_populates="character")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
from django.db import models
from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Coche(Base):
    __tablename__ = "coches"

    matricula = Column(String, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)

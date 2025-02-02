from sqlalchemy import Column, Integer, String, JSON
from geoalchemy2 import Geometry
from database import Base

class PointData(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(Geometry("POINT"), nullable=False)  # Use Geometry type
    description = Column(String(255),nullable=True)

class PolygonData(Base):
    __tablename__ = "polygons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    boundary = Column(Geometry("POLYGON"), nullable=False)  # Use Geometry type
    info = Column(JSON,nullable= True)

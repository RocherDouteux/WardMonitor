from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class RegionDB(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    region_name = Column(String, unique=True, index=True)
    wards = relationship("WardDB", back_populates="region", cascade="all, delete-orphan")

class WardDB(Base):
    __tablename__ = "wards"
    id = Column(Integer, primary_key=True, index=True)
    ward_id = Column(Integer, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"))
    region = relationship("RegionDB", back_populates="wards")
    plots = relationship("PlotDB", back_populates="ward", cascade="all, delete-orphan")

class PlotDB(Base):
    __tablename__ = "plots"
    id = Column(Integer, primary_key=True, index=True)
    plot_number = Column(Integer, index=True)  # 1 to 60
    price = Column(Integer)
    size = Column(String)
    available = Column(Boolean, default=True)
    ward_id = Column(Integer, ForeignKey("wards.id"))
    ward = relationship("WardDB", back_populates="plots")

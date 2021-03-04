from sqlalchemy import Column, Integer, ForeignKey

from ..base import Base


class CarHasColor(Base):
    __tablename__ = 'car_has_color'

    car_id = Column(Integer,
                    ForeignKey('cars.id', ondelete="CASCADE"),
                    primary_key=True)
    color_id = Column(Integer,
                      ForeignKey('colors.id', ondelete="CASCADE"),
                      primary_key=True)

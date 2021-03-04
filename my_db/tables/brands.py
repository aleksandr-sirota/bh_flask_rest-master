from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base


class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable= False)
    country = Column(String(100), nullable=False)
    cars = relationship('Car',
                        backref='brand',
                        # back_populates='brand',
                        cascade="all, delete",
                        passive_deletes=True
                        )

    def __repr__(self):
        return f"<Brand(id={self.brand_id}, title='{self.title}', " \
               f"country='{self.country}')>"

    def to_dict(self):
        return {
            'id': self.brand_id,
            'title': self.title,
            'country': self.country,
            'cars': [car.to_dict() for car in self.cars]
        }

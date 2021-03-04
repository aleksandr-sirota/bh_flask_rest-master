from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Car(Base):
    __tablename__ = 'cars'

    car_id = Column('id', Integer, primary_key=True, autoincrement=True)
    model = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete="CASCADE"))
    colors = relationship("Color",
                          secondary='car_has_color',
                          backref="cars",
                          cascade="all, delete",
                          passive_deletes=True)

    def __repr__(self):
        return f"<Car(id={self.car_id}, model='{self.model}', price={self.price})>"

    def to_dict(self):
        return {
            'id': self.car_id,
            'model': self.model,
            'price': self.price,
            'colors': [color.to_dict() for color in self.colors]
        }

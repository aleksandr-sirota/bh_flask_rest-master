from sqlalchemy import Column, Integer, String

from ..base import Base


class Color(Base):
    __tablename__ = 'colors'

    color_id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)

    def __repr__(self):
        return f"Color(id={self.color_id}, title='{self.title}')"

    def to_dict(self):
        return {
            'id': self.color_id,
            'title': self.title
        }

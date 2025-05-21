
import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import relationship

from app.db.session import Base

class InventoryItem(Base):
    __tablename__ = "inventory_item"

    product_id = Column(Integer, ForeignKey("product.id"), primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("location.id"), primary_key=True, index=True)

    quantity = Column(Integer, nullable=False, default=0)
    reorder_point = Column(Integer, nullable=False, default=0)
    last_updated = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc), onupdate=func.now())

    product = relationship("Product", back_populates="inventory_items")
    location = relationship("Location", back_populates="inventory_item")

    def __repr__(self):
        return f"{type(self).__name__}(product_id={self.product_id}, location_id={self.location_id}, quantity={self.quantity})"
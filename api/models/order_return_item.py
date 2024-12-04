from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Float, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.order_return import OrderReturn
    from models.store_product import StoreProduct


class OrderReturnItem(Base):
    """
    OrderReturnItem model.
    """

    __tablename__ = "OrderReturnItem"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    return_id = mapped_column(
        ForeignKey("OrderReturn.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    product_id = mapped_column(
        ForeignKey("StoreProduct.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    quantity = mapped_column(Float, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    product: Mapped["StoreProduct"] = relationship(
        "StoreProduct", back_populates="OrderReturnItem"
    )
    return_: Mapped["OrderReturn"] = relationship(
        "OrderReturn", back_populates="OrderReturnItem"
    )

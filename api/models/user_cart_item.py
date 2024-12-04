from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Float, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store_product import StoreProduct
    from models.user_cart import UserCart


class UserCartItem(Base):
    """
    UserCartItem model.
    """

    __tablename__ = "UserCartItem"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    cart_id = mapped_column(
        ForeignKey("UserCart.id", ondelete="CASCADE", onupdate="CASCADE"),
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
    secondary_action = mapped_column(Text)

    cart: Mapped["UserCart"] = relationship("UserCart", back_populates="UserCartItem")
    product: Mapped["StoreProduct"] = relationship(
        "StoreProduct", back_populates="UserCartItem"
    )

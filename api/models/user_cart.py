from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store
    from models.user import User
    from models.user_cart_item import UserCartItem
    from models.user_order import UserOrder


class UserCart(Base):
    """
    UserCart model.
    """

    __tablename__ = "UserCart"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    user_id = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    store: Mapped["Store"] = relationship("Store", back_populates="UserCart")
    user: Mapped["User"] = relationship("User", back_populates="UserCart")
    UserOrder: Mapped[List["UserOrder"]] = relationship(
        "UserOrder", uselist=True, back_populates="cart"
    )
    UserCartItem: Mapped[List["UserCartItem"]] = relationship(
        "UserCartItem", uselist=True, back_populates="cart"
    )

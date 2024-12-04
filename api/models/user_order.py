from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Float, ForeignKey, Index, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.pickup_slot import PickupSlot
    from models.store import Store
    from models.user import User
    from models.user_cart import UserCart
    from models.order_return import OrderReturn
    from models.payment_transaction import PaymentTransaction
    from models.store_review import StoreReview


class UserOrder(Base):
    """
    UserOrder model.
    """

    __tablename__ = "UserOrder"
    __table_args__ = (Index("UserOrder_cart_id_key", "cart_id", unique=True),)

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    user_id = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    cart_id = mapped_column(
        ForeignKey("UserCart.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    pickup_slot_id = mapped_column(
        ForeignKey("PickupSlot.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    total = mapped_column(Float, nullable=False)
    status = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    cart: Mapped["UserCart"] = relationship("UserCart", back_populates="UserOrder")
    pickup_slot: Mapped["PickupSlot"] = relationship(
        "PickupSlot", back_populates="UserOrder"
    )
    store: Mapped["Store"] = relationship("Store", back_populates="UserOrder")
    user: Mapped["User"] = relationship("User", back_populates="UserOrder")
    OrderReturn: Mapped[List["OrderReturn"]] = relationship(
        "OrderReturn", uselist=True, back_populates="order"
    )
    PaymentTransaction: Mapped[List["PaymentTransaction"]] = relationship(
        "PaymentTransaction", uselist=True, back_populates="order"
    )
    StoreReview: Mapped[List["StoreReview"]] = relationship(
        "StoreReview", uselist=True, back_populates="order"
    )

from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Float, ForeignKey, Index, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.user_order import UserOrder


class PaymentTransaction(Base):
    """
    PaymentTransaction model.
    """

    __tablename__ = "PaymentTransaction"
    __table_args__ = (
        Index("PaymentTransaction_order_id_key", "order_id", unique=True),
        Index("PaymentTransaction_stripe_id_key", "stripe_id", unique=True),
    )

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    order_id = mapped_column(
        ForeignKey("UserOrder.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    stripe_id = mapped_column(Text, nullable=False)
    amount = mapped_column(Float, nullable=False)
    currency = mapped_column(Text, nullable=False)
    status = mapped_column(Text, nullable=False)
    type = mapped_column(Text, nullable=False)
    method = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    order: Mapped["UserOrder"] = relationship(
        "UserOrder", back_populates="PaymentTransaction"
    )

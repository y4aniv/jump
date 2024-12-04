from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.user_order import UserOrder


class OrderReturn(Base):
    """
    OrderReturn model.
    """

    __tablename__ = "OrderReturn"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    order_id = mapped_column(
        ForeignKey("UserOrder.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    reason = mapped_column(Text, nullable=False)
    status = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    description = mapped_column(Text)

    order: Mapped["UserOrder"] = relationship("UserOrder", back_populates="OrderReturn")
    OrderReturnItem: Mapped[List["OrderReturnItem"]] = relationship(
        "OrderReturnItem", uselist=True, back_populates="return_"
    )

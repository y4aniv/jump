from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Index, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store
    from models.user_order import UserOrder


class StoreReview(Base):
    """
    StoreReview model.
    """

    __tablename__ = "StoreReview"
    __table_args__ = (Index("StoreReview_order_id_key", "order_id", unique=True),)

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    order_id = mapped_column(
        ForeignKey("UserOrder.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    rating = mapped_column(Integer, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    review = mapped_column(Text)

    order: Mapped["UserOrder"] = relationship("UserOrder", back_populates="StoreReview")
    store: Mapped["Store"] = relationship("Store", back_populates="StoreReview")

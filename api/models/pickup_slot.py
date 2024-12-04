from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store
    from models.user_order import UserOrder


class PickupSlot(Base):
    """
    PickupSlot model.
    """

    __tablename__ = "PickupSlot"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    start_time = mapped_column(DateTime, nullable=False)
    end_time = mapped_column(DateTime, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    store: Mapped["Store"] = relationship("Store", back_populates="PickupSlot")
    UserOrder: Mapped[List["UserOrder"]] = relationship(
        "UserOrder", uselist=True, back_populates="pickup_slot"
    )

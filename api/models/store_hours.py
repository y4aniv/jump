from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store


class StoreHours(Base):
    """
    StoreHours model.
    """

    __tablename__ = "StoreHours"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    day = mapped_column(Integer, nullable=False)
    is_open = mapped_column(Boolean, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    open_at = mapped_column(DateTime)
    close_at = mapped_column(DateTime)

    store: Mapped["Store"] = relationship("Store", back_populates="StoreHours")

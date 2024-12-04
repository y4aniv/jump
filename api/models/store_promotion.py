from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store


class StorePromotion(Base):
    """
    StorePromotion model.
    """

    __tablename__ = "StorePromotion"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    name = mapped_column(Text, nullable=False)
    discount_type = mapped_column(Text, nullable=False)
    discount_value = mapped_column(Float, nullable=False)
    start_date = mapped_column(DateTime, nullable=False)
    end_date = mapped_column(DateTime, nullable=False)
    is_active = mapped_column(Boolean, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    description = mapped_column(Text)

    store: Mapped["Store"] = relationship("Store", back_populates="StorePromotion")
    StoreCategoryPromotion: Mapped[List["StoreCategoryPromotion"]] = relationship(
        "StoreCategoryPromotion", uselist=True, back_populates="promotion"
    )
    StoreProductPromotion: Mapped[List["StoreProductPromotion"]] = relationship(
        "StoreProductPromotion", uselist=True, back_populates="promotion"
    )

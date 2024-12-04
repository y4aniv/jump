from typing import TYPE_CHECKING, List, Optional
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store
    from models.store_category_promotion import StoreCategoryPromotion
    from models.store_product import StoreProduct


class StoreCategory(Base):
    """
    StoreCategory model.
    """

    __tablename__ = "StoreCategory"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    name = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    description = mapped_column(Text)
    parent_id = mapped_column(
        ForeignKey("StoreCategory.id", ondelete="SET NULL", onupdate="CASCADE")
    )

    parent: Mapped[Optional["StoreCategory"]] = relationship(
        "StoreCategory", remote_side=[id], back_populates="parent_reverse"
    )
    parent_reverse: Mapped[List["StoreCategory"]] = relationship(
        "StoreCategory", uselist=True, remote_side=[parent_id], back_populates="parent"
    )
    store: Mapped["Store"] = relationship("Store", back_populates="StoreCategory")
    StoreCategoryPromotion: Mapped[List["StoreCategoryPromotion"]] = relationship(
        "StoreCategoryPromotion", uselist=True, back_populates="category"
    )
    StoreProduct: Mapped[List["StoreProduct"]] = relationship(
        "StoreProduct", uselist=True, back_populates="category"
    )

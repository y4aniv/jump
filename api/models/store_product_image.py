from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store_product import StoreProduct


class StoreProductImage(Base):
    """
    StoreProductImage model.
    """

    __tablename__ = "StoreProductImage"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    product_id = mapped_column(
        ForeignKey("StoreProduct.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    url = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    alt_text = mapped_column(Text)

    product: Mapped["StoreProduct"] = relationship(
        "StoreProduct", back_populates="StoreProductImage"
    )

from typing import TYPE_CHECKING, List, Optional
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Float, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store
    from models.store_category import StoreCategory
    from models.store_product_image import StoreProductImage
    from models.store_product_metadata import StoreProductMetadata
    from models.store_product_promotion import StoreProductPromotion
    from models.store_product_tag import StoreProductTag
    from models.user_cart_item import UserCartItem
    from models.order_return_item import OrderReturnItem


class StoreProduct(Base):
    """
    StoreProduct model.
    """

    __tablename__ = "StoreProduct"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    name = mapped_column(Text, nullable=False)
    price = mapped_column(Float, nullable=False)
    sku = mapped_column(Text, nullable=False)
    status = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    category_id = mapped_column(
        ForeignKey("StoreCategory.id", ondelete="SET NULL", onupdate="CASCADE")
    )
    description = mapped_column(Text)
    quantity = mapped_column(Float)
    unit = mapped_column(Text)

    category: Mapped[Optional["StoreCategory"]] = relationship(
        "StoreCategory", back_populates="StoreProduct"
    )
    store: Mapped["Store"] = relationship("Store", back_populates="StoreProduct")
    StoreProductImage: Mapped[List["StoreProductImage"]] = relationship(
        "StoreProductImage", uselist=True, back_populates="product"
    )
    StoreProductMetadata: Mapped[List["StoreProductMetadata"]] = relationship(
        "StoreProductMetadata", uselist=True, back_populates="product"
    )
    StoreProductPromotion: Mapped[List["StoreProductPromotion"]] = relationship(
        "StoreProductPromotion", uselist=True, back_populates="product"
    )
    StoreProductTag: Mapped[List["StoreProductTag"]] = relationship(
        "StoreProductTag", uselist=True, back_populates="product"
    )
    UserCartItem: Mapped[List["UserCartItem"]] = relationship(
        "UserCartItem", uselist=True, back_populates="product"
    )
    OrderReturnItem: Mapped[List["OrderReturnItem"]] = relationship(
        "OrderReturnItem", uselist=True, back_populates="product"
    )

from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Float, Index, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.notification import Notification
    from models.pickup_slot import PickupSlot
    from models.store_category import StoreCategory
    from models.store_hours import StoreHours
    from models.store_local_settings import StoreLocalSettings
    from models.store_promotion import StorePromotion
    from models.store_product import StoreProduct
    from models.store_review import StoreReview
    from models.store_user import StoreUser
    from models.user_cart import UserCart
    from models.user_favorite import UserFavorite
    from models.user_order import UserOrder


class Store(Base):
    """
    Store model.
    """

    __tablename__ = "Store"
    __table_args__ = (Index("Store_stripe_id_key", "stripe_id", unique=True),)

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    short_name = mapped_column(Text, nullable=False)
    legal_name = mapped_column(Text, nullable=False)
    address = mapped_column(Text, nullable=False)
    city = mapped_column(Text, nullable=False)
    state = mapped_column(Text, nullable=False)
    zip = mapped_column(Text, nullable=False)
    country = mapped_column(Text, nullable=False)
    phone = mapped_column(Text, nullable=False)
    email = mapped_column(Text, nullable=False)
    logo = mapped_column(Text, nullable=False)
    pricing_level = mapped_column(Integer, nullable=False)
    status = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    description = mapped_column(Text)
    latitude = mapped_column(Float)
    longitude = mapped_column(Float)
    website = mapped_column(Text)
    pickup_note = mapped_column(Text)
    stripe_id = mapped_column(Text)

    Notification: Mapped[List["Notification"]] = relationship(
        "Notification", uselist=True, back_populates="store"
    )
    PickupSlot: Mapped[List["PickupSlot"]] = relationship(
        "PickupSlot", uselist=True, back_populates="store"
    )
    StoreCategory: Mapped[List["StoreCategory"]] = relationship(
        "StoreCategory", uselist=True, back_populates="store"
    )
    StoreHours: Mapped[List["StoreHours"]] = relationship(
        "StoreHours", uselist=True, back_populates="store"
    )
    StoreLocalSettings: Mapped[List["StoreLocalSettings"]] = relationship(
        "StoreLocalSettings", uselist=True, back_populates="store"
    )
    StorePromotion: Mapped[List["StorePromotion"]] = relationship(
        "StorePromotion", uselist=True, back_populates="store"
    )
    StoreUser: Mapped[List["StoreUser"]] = relationship(
        "StoreUser", uselist=True, back_populates="store"
    )
    UserCart: Mapped[List["UserCart"]] = relationship(
        "UserCart", uselist=True, back_populates="store"
    )
    UserFavorite: Mapped[List["UserFavorite"]] = relationship(
        "UserFavorite", uselist=True, back_populates="store"
    )
    StoreProduct: Mapped[List["StoreProduct"]] = relationship(
        "StoreProduct", uselist=True, back_populates="store"
    )
    UserOrder: Mapped[List["UserOrder"]] = relationship(
        "UserOrder", uselist=True, back_populates="store"
    )
    StoreReview: Mapped[List["StoreReview"]] = relationship(
        "StoreReview", uselist=True, back_populates="store"
    )

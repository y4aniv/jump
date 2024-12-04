from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Index, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.notification import Notification
    from models.store_user import StoreUser
    from models.user_cart import UserCart
    from models.user_favorite import UserFavorite
    from models.user_order import UserOrder
    from models.user_reset_password import UserResetPassword
    from models.user_session import UserSession


class User(Base):
    """
    User model.
    """

    __tablename__ = "User"
    __table_args__ = (Index("User_email_key", "email", unique=True),)

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    first_name = mapped_column(Text, nullable=False)
    last_name = mapped_column(Text, nullable=False)
    email = mapped_column(Text, nullable=False)
    password = mapped_column(Text, nullable=False)
    avatar = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    Notification: Mapped[List["Notification"]] = relationship(
        "Notification", uselist=True, back_populates="user"
    )
    StoreUser: Mapped[List["StoreUser"]] = relationship(
        "StoreUser", uselist=True, back_populates="user"
    )
    UserCart: Mapped[List["UserCart"]] = relationship(
        "UserCart", uselist=True, back_populates="user"
    )
    UserFavorite: Mapped[List["UserFavorite"]] = relationship(
        "UserFavorite", uselist=True, back_populates="user"
    )
    UserResetPassword: Mapped[List["UserResetPassword"]] = relationship(
        "UserResetPassword", uselist=True, back_populates="user"
    )
    UserSession: Mapped[List["UserSession"]] = relationship(
        "UserSession", uselist=True, back_populates="user"
    )
    UserOrder: Mapped[List["UserOrder"]] = relationship(
        "UserOrder", uselist=True, back_populates="user"
    )

from typing import TYPE_CHECKING, Optional
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import Boolean, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.store import Store
    from models.user import User


class Notification(Base):
    """
    Notification model.
    """

    __tablename__ = "Notification"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    title = mapped_column(Text, nullable=False)
    message = mapped_column(Text, nullable=False)
    type = mapped_column(Text, nullable=False)
    is_read = mapped_column(Boolean, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
    user_id = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    link = mapped_column(Text)

    store: Mapped[Optional["Store"]] = relationship(
        "Store", back_populates="Notification"
    )
    user: Mapped[Optional["User"]] = relationship("User", back_populates="Notification")

from typing import TYPE_CHECKING
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.role import Role
    from models.store import Store
    from models.user import User


class StoreUser(Base):
    """
    StoreUser model.
    """

    __tablename__ = "StoreUser"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    store_id = mapped_column(
        ForeignKey("Store.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    user_id = mapped_column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    role_id = mapped_column(
        ForeignKey("Role.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    role: Mapped["Role"] = relationship("Role", back_populates="StoreUser")
    store: Mapped["Store"] = relationship("Store", back_populates="StoreUser")
    user: Mapped["User"] = relationship("User", back_populates="StoreUser")

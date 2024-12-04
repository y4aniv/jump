from typing import TYPE_CHECKING, List
from uuid import uuid4

from extensions.sqlalchemy import Base
from sqlalchemy import DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    pass


class Role(Base):
    """
    Role model.
    """

    __tablename__ = "Role"

    id = mapped_column(Text, primary_key=True, default=lambda: str(uuid4()))
    name = mapped_column(Text, nullable=False)
    workflow = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    StoreUser: Mapped[List["StoreUser"]] = relationship(
        "StoreUser", uselist=True, back_populates="role"
    )

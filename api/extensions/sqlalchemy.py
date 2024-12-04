from typing import TYPE_CHECKING, Any, Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

if TYPE_CHECKING:
    from sqlalchemy.ext.declarative import DeclarativeMeta
    from sqlalchemy.orm.session import Session as SessionType

engine = create_engine("sqlite:///storage/database/default.db", pool_pre_ping=True)

SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)

Base = declarative_base()
Base.metadata.create_all(engine)


def __repr__(self) -> str:
    """
    Return a string representation of the object.

    :return: The string representation of the object.
    """
    return f"<{self.__class__.__name__} {getattr(self, 'id', 'No ID')}>"


def save(self, session: "SessionType" = None) -> "DeclarativeMeta":
    """
    Save the object to the database.

    :param session: The session to use for saving the object.

    :return: The saved object.
    """
    if session is None:
        session = Session()

    session.add(self)
    session.commit()
    return self


def delete(self, session: "SessionType" = None) -> None:
    """
    Delete the object from the database.

    :param session: The session to use for deleting the object.
    """
    if session is None:
        session = Session()

    session.delete(self)
    session.commit()


def to_dict(self) -> Dict[str, Any]:
    """
    Convert the object to a dictionary.

    :return: The dictionary representation of the object.
    """
    return {
        column.name: getattr(self, column.name) for column in self.__table__.columns
    }


Base.__repr__ = __repr__
Base.save = save
Base.delete = delete
Base.to_dict = to_dict

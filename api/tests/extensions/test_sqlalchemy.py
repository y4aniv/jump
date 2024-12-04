import unittest

from extensions.sqlalchemy import Base, Session, engine
from sqlalchemy import Column, Integer, String


class User(Base):
    """
    A user model.
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class TestSQLAlchemyExtensions(unittest.TestCase):
    """
    Test the SQLAlchemy extensions.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        Base.metadata.create_all(engine)
        self.session = Session()

    def tearDown(self):
        """
        Tear down the test case.
        """
        self.session.close()
        self.session.rollback()

    def test_save(self):
        """
        Test saving an object.
        """
        user = User(name="Test User")
        user.save(self.session)
        saved_user = self.session.query(User).filter_by(name="Test User").first()
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user.name, "Test User")


if __name__ == "__main__":
    unittest.main()

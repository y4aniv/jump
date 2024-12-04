import unittest

from sqlalchemy import Column, Integer, String
from utils.orm import Base, Session, engine


class TestModel(Base):
    """
    Test model for ORM testing.
    """

    __tablename__ = "test_model"
    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(engine)


class TestORM(unittest.TestCase):
    """
    Test cases for ORM utility functions.
    """

    def setUp(self):
        """
        Setup method to create a session.
        """
        self.session = Session()

    def tearDown(self):
        """
        Teardown method to rollback and close the session.
        """
        self.session.rollback()
        self.session.close()

    def test_save(self):
        """
        Test case to save an object to the database.
        """
        test_instance = TestModel(name="Test Name")
        saved_instance = test_instance.save(session=self.session)
        self.assertIsNotNone(saved_instance.id)
        self.assertEqual(saved_instance.name, "Test Name")

        retrieved_instance = self.session.query(TestModel).get(saved_instance.id)
        self.assertIsNotNone(retrieved_instance)
        self.assertEqual(retrieved_instance.name, "Test Name")


if __name__ == "__main__":
    unittest.main()

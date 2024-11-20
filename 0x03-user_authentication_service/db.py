#!/usr/bin/env python3
"""
DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError, NoResultFound


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new database instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a user to the database
        """
        # Create a new User instance
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the user to the current session
        session = self._session
        session.add(new_user)

        # Commit the session to save the user in the database
        session.commit()

        # Return the newly created user
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find user by ID method
        """
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError()

        new_user = self._session.query(User).filter_by(**kwargs).first()

        if new_user:
            return new_user
        raise NoResultFound()

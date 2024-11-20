#!/usr/bin/env python3
"""
Creates a SQLAlchemy model named User for a database
table named users.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    Creates a table for users
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)


if __name__ == "__main__":
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}.".format(column, column.type))

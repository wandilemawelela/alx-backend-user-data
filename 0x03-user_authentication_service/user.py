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
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)


# Example of creating an SQLite database and adding a user
if __name__ == "__main__":
    # Replace 'sqlite:///example.db' with your database URL
    engine = create_engine('sqlite:///example.db', echo=True)

    # Create the users table
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new user
    new_user = User(email="user@example.com", hashed_password="hashedpassword123")

    # Add the user to the session and commit the transaction
    session.add(new_user)
    session.commit()

    # Query the database
    users = session.query(User).all()
    for user in users:
        print(user.id, user.email)

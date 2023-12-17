# generator.py

import argparse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker

# Define a base class for declarative models in SQLAlchemy
Base = declarative_base()

# Define a User class representing the 'users' table in the database
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    address=Column(String)
    license=Column(String)
    bank=Column(String)

# Define a Post class representing the 'posts' table in the database
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

# Function to generate fake user data and add it to the database
def generate_fake_data(session, num_users=10):
  
    fake = Faker(['it_IT'])

    for _ in range(num_users):
        user = User(name=fake.name(), email=fake.email(),address=fake.address(),license=fake.license_plate(),bank=fake.iban())
        session.add(user)

    session.commit()

# Function to generate the database and populate it with fake data
def generate_database(engine_url):
    engine = create_engine(engine_url)
    # Create tables defined in the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Generate fake data and add it to the database
    generate_fake_data(session)

# Entry point for the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a container image with fake data for a relational database.")
    parser.add_argument("--database-url", type=str, default="sqlite:///fake_data.db", help="URL of the database for SQLAlchemy.")
    parser.add_argument("--num-users", type=int, default=10, help="Number of fake users to generate.")
   

    args = parser.parse_args()

    # Generate the database with fake data using the specified database URL
    generate_database(args.database_url)
    print(f"Se generaron datos falsos en la base de datos: {args.database_url}")
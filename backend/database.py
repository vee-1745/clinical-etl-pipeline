from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib.parse

# 1. Safely encode your exact password
password = urllib.parse.quote_plus("Vedant@windows.1745")

# 2. Inject the safe password into the PostgreSQL connection string
DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/clinical_dwh"

# Create the SQLAlchemy Engine (The bridge to the database)
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class (Each instance is a conversation with the DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models
Base = declarative_base()

# Dependency to get the DB session in our API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
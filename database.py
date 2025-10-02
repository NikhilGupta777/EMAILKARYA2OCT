import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Get the database URL from the environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Check if the database URL is set
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("No DATABASE_URL found in environment variables")

# Railway/Neon PostgreSQL: Ensure proper SSL and connection pooling
connect_args = {}
if "postgresql" in SQLALCHEMY_DATABASE_URL:
    # Add SSL mode if not already in URL
    if "sslmode" not in SQLALCHEMY_DATABASE_URL:
        connect_args["sslmode"] = "require"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,  # Verify connections before using
    pool_recycle=300,    # Recycle connections every 5 minutes
    pool_size=10,        # Connection pool size
    max_overflow=20      # Max overflow connections
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
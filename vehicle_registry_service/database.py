from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:20021225@localhost/dmt_users"
DATABASE_URL = "postgresql://postgres:20021225@db.uxzsljrsotdndfbbseki.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
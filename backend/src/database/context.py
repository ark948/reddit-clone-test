from src.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from contextlib import contextmanager



engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = DeclarativeBase()



@contextmanager
def SessionManager():
    db = SessionLocal()
    try:
        yield db
    except:
        # if we fail somehow rollback the connection
        print("\n----> [DB Context failed.]\n")
        db.rollback()
        raise
    finally:
        db.close()



# somewhere where a session is needed
# import database

# with database.SessionManager() as db:
#     # your code using the database connection goes here
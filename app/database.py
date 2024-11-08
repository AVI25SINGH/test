from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database connection    %40 --@
DATABSE_URL="mysql+pymysql://root:AVInash12%40#@localhost/library_db"

engin=create_engine(DATABSE_URL)
session=sessionmaker(autocommit=False,autoflush=False,bind=engin)
# sessionmaker is a function provided by SQLAlchemy to create a session factory.
# A session factory is used to create individual session instances. Each session instance represents a temporary connection
# to the database, where you can perform CRUD (Create, Read, Update, Delete) operations in a transaction.

# Flushing means that any pending changes (e.g., newly added or modified objects in the session) are sent to the
# database before executing any further SQL statements, so the queries reflect the current state.

# The bind parameter binds this session to a specific database engine.

# The sessionmaker() call returns a session factory, a callable that creates new sessions when called.


Base = declarative_base()

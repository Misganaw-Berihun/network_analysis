from sqlalchemy import create_engine, MetaData

import pandas as pd
from sqlalchemy import create_engine
import os
import sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.postgrsql.postgresql_connect import create_database_engine
from sqlalchemy import create_engine, MetaData

# Replace 'your_database_url' with your actual database connection URL
database_url = 'postgresql://username:password@localhost/your_database'
engine = create_database_engine()

# Create a metadata object
metadata = MetaData()

# Reflect existing tables and associate them with the engine
metadata.reflect(bind=engine)

# Drop all tables
for table in reversed(metadata.sorted_tables):
    table.drop(bind=engine)

connection = engine.connect()
# Optional: Commit changes if you want to persist the changes immediately
connection.commit()
connection.close()


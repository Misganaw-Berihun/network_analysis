from sqlalchemy import create_engine, MetaData, inspect

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
inspector = inspect(engine)

# Get the table names
table_names = inspector.get_table_names()

# Print the table names
for table_name in table_names:
    print(table_name)
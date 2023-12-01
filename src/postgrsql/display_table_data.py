import pandas as pd
from sqlalchemy import create_engine
import os
import sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.postgrsql.postgresql_connect import create_database_engine

database_url = 'your_actual_database_url'
engine = create_database_engine()

table_name = 'message_table'
query = f'SELECT * FROM {table_name}'
df = pd.read_sql(query, engine)

print(df)

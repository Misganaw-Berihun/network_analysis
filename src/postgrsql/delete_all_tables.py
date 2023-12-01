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

database_url = 'postgresql://username:password@localhost/your_database'
engine = create_database_engine()

metadata = MetaData()

metadata.reflect(bind=engine)

for table in reversed(metadata.sorted_tables):
    table.drop(bind=engine)

connection = engine.connect()
connection.commit()
connection.close()


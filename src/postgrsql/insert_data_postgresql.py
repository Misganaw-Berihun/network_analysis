import os
import sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)
    
import pandas as pd
from sqlalchemy import create_engine
from src.postgrsql.postgresql_connect import create_database_engine
from src.postgrsql.create_tables_postgresql import create_tables

import os
import sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader

def map_dataframe_to_user_table(engine, dataframe):
    table_name = 'user_table'
    dataframe.to_sql(table_name, engine, index=True, if_exists='replace')

def map_dataframe_to_reaction_table(engine, dataframe):
    table_name = 'reaction_table'
    dataframe.to_sql(table_name, engine, index=False, if_exists='replace')

def map_dataframe_to_message_table(engine, dataframe):
    table_name = 'message_table'
    dataframe.to_sql(table_name, engine, index=False, if_exists='replace')

if __name__ == "__main__":
    sl = SlackDataLoader()
    user_df = sl.create_users_df()
    reaction_df = sl.create_reaction_data_frame()
    message_df = sl.create_dataframe()

    engine = create_database_engine()
    create_tables(engine)
    map_dataframe_to_user_table(engine, user_df)
    map_dataframe_to_reaction_table(engine, reaction_df)
    map_dataframe_to_message_table(engine, message_df)


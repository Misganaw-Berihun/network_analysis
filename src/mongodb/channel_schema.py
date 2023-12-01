import os
import sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.mongodb.message_schema import get_message_schema
def get_channel_schema():
    return {
        "name": str,
        "date": str,
        "messages": [get_message_schema()],
    }
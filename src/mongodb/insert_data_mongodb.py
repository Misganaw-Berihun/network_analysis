import os
import sys
from src.loader import SlackDataLoader
from src.mongodb.message_schema import get_message_schema
from src.mongodb.mongodb_connection import get_database

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

def insert_message_into_channel(channel_name, date, message):
    db = get_database()
    channels_collection = db["channels_data"]

    channel_data = {
        "name": channel_name,
        "date": date,
        "message": message,
    }

    channels_collection.insert_one(channel_data)

def read_files():
    sl = SlackDataLoader('../../data/anonymized/')
    js_files = sl.read_json_files()

    for file in js_files:
        for channel_name, data_list in file.items():
            for d in data_list:
                for json_data in d.get('msg', []):
                    try:
                        client_msg_id = json_data.get('client_msg_id')
                        type_ = json_data.get('type')
                        subtype = json_data.get('subtype')
                        ts = json_data.get('ts')
                        user = json_data.get('user')
                        text = json_data.get('text')
                        blocks = json_data.get('blocks', [])
                        team = json_data.get('team')
                        user_team = json_data.get('user_team')
                        source_team = json_data.get('source_team')
                        user_profile = json_data.get('user_profile', {})

                        message_schema = get_message_schema()
                        # Validate against the schema if needed

                        mapped_message = {
                            "client_msg_id": client_msg_id,
                            "type": type_,
                            "subtype": subtype,
                            "ts": ts,
                            "user": user,
                            "text": text,
                            "blocks": blocks,
                            "team": team,
                            "user_team": user_team,
                            "source_team": source_team,
                            "user_profile": user_profile,
                        }

                        insert_message_into_channel(channel_name, d.get('sent_date'), mapped_message)
                    except Exception as e:
                        print(f"Error processing message: {e}")

if __name__ == "__main__":
    read_files()

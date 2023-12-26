import json
from pathlib import Path
from typing import Union
import os
import sys
from copy import deepcopy

DB_PATH = 'database/users_db.json'

user_dict_template = {
    'page': 1,
    'bookmarks': set()
}

def write_db_to_json(users_db: dict[dict[str, Union[int, set[int]]]],
                     path: Path = DB_PATH):
    users_db_json = deepcopy(users_db)
    for user in users_db_json:
        users_db_json[user]['bookmarks'] = list(users_db_json[user]['bookmarks'])
    with open(path, 'w', encoding='utf-8') as db_file:
        json.dump(users_db_json, db_file, indent=4)


def read_db_from_json(path: Path = DB_PATH):
    users_db = {}
    with open(path, 'r', encoding='utf-8') as db_file:
        users_db_json = json.load(db_file)

    for k, v in users_db_json.items():
        users_db[int(k)] = v
        users_db[int(k)]['bookmarks'] = set(users_db[int(k)]['bookmarks'])
    return users_db


if os.path.exists(os.path.join(sys.path[0], os.path.normpath(DB_PATH))):
    users_db = read_db_from_json()
else:
    users_db = {}

pass
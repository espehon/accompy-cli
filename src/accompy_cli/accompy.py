# Copyright (c) 2023, espehon
# License: https://www.gnu.org/licenses/gpl-3.0.html

import os
import json


# storage_path = os.path.expanduser("~/.local/share/accompy/storage.json")
storage_path = os.path.expanduser("~/github/accompy/tests/base.json")

with open(storage_path, 'r') as f:
    data = json.load(f)

print(data[1]['title'])
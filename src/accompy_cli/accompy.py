# Copyright (c) 2023, espehon
# License: https://www.gnu.org/licenses/gpl-3.0.html

import os
import json
from colorama import Fore, init


# template for new entries. Not to be used for anything else: Not even as a header unless used as a starting point. This should be moved to json in ~/.config eventually.
template = ['title', 'start date', 'end date', 'situation', 'action', 'result']

# storage_path = os.path.expanduser("~/.local/share/accompy/storage.json")
storage_path = os.path.expanduser("~/github/accompy/tests/base.json")

with open(storage_path, 'r') as f:
    data = json.load(f)



# Build header
header = template
for entry in data:
    for key in entry:
        if key not in header:
            header.append(key)

# Build body
body = []
for index, entry in enumerate(data):
    body.append([])
    for column in header:
        if column in entry:
            body[index].append(entry[column])
        else:
            body[index].append('')

# Calculate column widths
padding = 4
widths = []
for title in header:
    widths.append(len(title) + padding)
for row in body:
    for index, size in enumerate(widths):
        if len(row[index]) > size:
            widths[index] = len(row[index]) + padding



# Print table

output = ''
for index, column in enumerate(header):
    output += column.ljust(widths[index])
for row in body:
    output += '\n'
    for index, column in enumerate(row):
        output += column.ljust(widths[index])

print(output)

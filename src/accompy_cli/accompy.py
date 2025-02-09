# Copyright (c) 2025, espehon
# License: https://www.gnu.org/licenses/gpl-3.0.html

import sys
import os
import json
import argparse
import importlib.metadata


import questionary


try:
    __version__ = f"accompy {importlib.metadata.version('accompy_cli')} from accompy_cli"
except importlib.metadata.PackageNotFoundError:
    __version__ = "Package not installed..."


# Set file paths
storage_folder = os.path.expanduser("~/.local/share/accompy/")
storage_file = "accompy.json"
storage_path = storage_folder + storage_file

# Check if storage folder exists, create it if missing.
if os.path.exists(os.path.expanduser(storage_folder)) == False:
    os.makedirs(storage_folder)

# Check if storage file exists, create it if missing.
if os.path.exists(storage_path) == False:
    with open(storage_path, 'w', encoding='utf-8') as file:
        json.dump({}, file)

# read storage file
try:
    with open(storage_path, 'r') as file:
        data = json.load(file)
except ValueError:
    print(f"Error reading {storage_path}! Try deleting the file :(")
    sys.exit(1)


# Set argument parsing
parser = argparse.ArgumentParser(
    description="Accompy: Keep track of your accomplishments from the command line!",
    epilog="(epilog) Homepage: https://TODO",
    allow_abbrev=False,
    add_help=False,
    usage="TODO",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument('-?', '--help', action='help', help='Show this help message and exit.')
parser.add_argument('-v', '--version', action='version', version=__version__, help="Show package version and exit.")

parser.add_argument('-n', '--new', nargs=2, type=str, metavar=('N', 'V'), action='store', help='Create [N] with the value of [V]. (Overwrite existing)')
parser.add_argument('-l', '--long', action='store_true', help='Show entries in long format (all details).')
parser.add_argument('-r', '--rename', nargs=2, type=str, metavar=('O', 'N'), action='store', help='Rename [O] to [N].')
parser.add_argument('-d', '--delete', nargs='+', metavar=('N1', 'N2'), action='store', type=str, help='Delete [N1] etc.')
# parser.add_argument("name", nargs='?', help="Name of entry to fetch. (Case sensitive)")




def gather_field_values():
    user_info = {}
    
    user_info['start_date'] = questionary.text("Please enter the start date:").ask()
    user_info['complete_date'] = questionary.text("Please enter the completed date:").ask()
    user_info['situation'] = questionary.text("What was the situation?").ask()
    user_info['action'] = questionary.text("What was the action?").ask()
    user_info['result'] = questionary.text("What was the result?").ask()

    skill_list_string = questionary.text("Enter any skills learned or strengthened (comma separated):").ask()
    user_info['skills'] = [item.strip() for item in skill_list_string.split(",")]
    
    return user_info


def save_data(dictionary: dict) -> None:
    pass
    #TODO add save function

def add_new_entry(master: dict, entry: dict) -> dict:
    int_keys = [int(k) for k in master.keys()]
    next_key = max(int_keys) + 1
    master[str(next_key)] = entry
    return master
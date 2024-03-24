#!/usr/bin/env python3

import argparse
import os
from fuckoff.history_manager import delete_all_history, interactive_delete



def parse_args():
    parser = argparse.ArgumentParser(description="Manage your terminal history with style.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--all", action="store_true", help="Delete all history")
    group.add_argument("-i", "--interactive", action="store_true", help="Selectively delete history items")
    return parser.parse_args()

def delete_last_command():
    history_path = os.path.expanduser('~/.zsh_history')
    if not os.path.exists(history_path):
        print("History file not found.")
        return

    with open(history_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    if lines:
        lines = lines[:-1]
        with open(history_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print("Last command deleted from history.")
    else:
        print("History is already empty.")

def main():
    args = parse_args()
    if args.all:
       delete_all_history()
    elif args.interactive:
       interactive_delete() 
    else:
        delete_last_command()

if __name__ == "__main__":
    main()

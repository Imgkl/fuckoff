#!/usr/bin/env python3

import argparse
import os
from fuckoff.history_manager import delete_all_history, interactive_delete, delete_last_command



def parse_args():
    parser = argparse.ArgumentParser(description="Manage your terminal history with style.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--all", action="store_true", help="Delete all history")
    group.add_argument("-i", "--interactive", action="store_true", help="Selectively delete history items")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.all:
       delete_all_history()
    elif args.interactive:
       interactive_delete() 
    else:
        delete_last_command()
        os.system('fc -R ~/.zsh_history')

if __name__ == "__main__":
    main()

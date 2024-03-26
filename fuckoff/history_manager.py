
import os
import questionary


def delete_last_command():
    history_path = os.path.expanduser('~/.zsh_history')
    if not os.path.exists(history_path):
        print("History file not found.")
        return

    with open(history_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    if len(lines) >= 2:
        lines = lines[:-2]
        with open(history_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print("Last command deleted from history")
    elif len(lines) == 1:
        lines = [] 
        with open(history_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print("Last command deleted from history")
    else:
        print("History is already empty.")

def delete_all_history():
    history_path = os.path.expanduser('~/.zsh_history')
    confirm = input("Are you sure you want to delete all history? This action cannot be undone. (y/N): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return

    if os.path.exists(history_path):
        with open(history_path, 'w'):
            pass

        print("All history has been deleted.")
    else:
        print("History file not found.")
    pass

def interactive_delete():
    history_path = os.path.expanduser('~/.zsh_history')
    if not os.path.exists(history_path):
        print("History file not found.")
        return

    with open(history_path, 'r', encoding='utf-8') as file:
        history_entries = [line.strip() for line in file.readlines()]

    selected_entries = questionary.checkbox(
        "Select history entries to delete:",
        choices=[{"name": entry} for entry in history_entries]
    ).ask()

    updated_history = [entry for entry in history_entries if entry not in selected_entries]

    with open(history_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(updated_history))
    if selected_entries.__len__() == 0:
        print("No entries selected.")
    else:
        print("Selected entries have been deleted.")

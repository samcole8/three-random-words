"""Load configuration, display menu and call functions."""

import json
import common
import wli


def get_config():
    """Fetch existing configuration file or create a new one."""
    try:
        with open("config.json", "r", encoding="utf-8") as config_file:
            config = json.loads(config_file.read())
    except FileNotFoundError:
        # Create new file and write the default configuration to it.
        with open("config.json", "w", encoding="utf-8") as config_file:
            config_file.write("{\"initiate\": 0, " +
                              "\"wordlist\": \"english3.txt\", " +
                              "\"word_count\": 3, " +
                              "\"developer_mode\": 0, " +
                              "\"pseudo_random\": 0}")
        # Recursively call this function until a valid file is opened.
        config = get_config()
    return config


def display_menu(menu_options, menu_title):
    """Display any menu."""
    print(menu_title)
    for value, option in enumerate(menu_options, start=1):
        print(f"[{value}] {option[0]}")


def start():
    """Display menu and call appropriate function."""
    config = get_config()
    terminate = False
    while terminate is False:
        menu_options = [
                        # New options below here.
                        ["Generate a password.", wli.generate],
                        ["Edit configuration."],
                        ["Cross-reference an existing password."],
                        ["Attempt to crack an existing password."],
                        ["Generate an average time-to-crack."],
                        ["Guess test."],
                        # Do not edit lines underneath.
                        ["Exit the program"]
                        ]
        display_menu(menu_options, "MAIN MENU")
        choice = common.integer_test("Select an option from the menu above",
                                     1,
                                     len(menu_options)
                                     )
        if choice == len(menu_options):
            terminate = True
        else:
            menu_options[choice - 1][1](config)


if __name__ == "__main__":
    start()

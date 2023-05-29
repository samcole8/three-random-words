"""Load configuration, display menu and call functions."""

import json
import common
import wli


def mod_config(config):
    """Modify configuration file"""
    menu_options = [
                    ["Change wordlist."],
                    ["Change word count."],
                    ["Toggle pseudo-randomness."],
                    # New options above.
                    ["Commit changes."],
                    ["Abort changes."]
                    ]
    modifying_config = True
    while modifying_config:
        display_menu(menu_options, "CONFIGURATION MENU")
        choice = common.integer_test("Select an option from the menu above",
                                     1,
                                     len(menu_options)
                                     )
        if choice == len(menu_options):
            print("Changes aborted.")
            modifying_config = False
        elif choice == len(menu_options) - 1:
            try:
                with open("config.json", "w", encoding="utf-8") as config_file:
                    config_file.write("{\"initiate\": " + str(config["initiate"]) + ", " +
                                      "\"wordlist\": \"" + config["wordlist"] + "\", " +
                                      "\"word_count\": " + str(config["word_count"]) + ", " +
                                      "\"developer_mode\": " + str(config["developer_mode"]) + ", " +
                                      "\"pseudo_random\": " + str(config["pseudo_random"]) + "}")
                print("Configuration updated.")
            except FileNotFoundError:
                common.error("Config file not found. Try deleting it.")
            modifying_config = False
        elif choice == 1:
            config["wordlist"] = "wordlists/" + input("Enter wordlist name :")
        elif choice == 2:
            word_count = common.integer_test("Enter new word count", 0)
            config["word_count"] = word_count
            print("Word count updated.")
        elif choice == 3:
            if config["pseudo_random"] == 1:
                print("Now using true random numbers.")
                config["pseudo_random"] = 0
            else:
                print("Now using pseudo-random numbers.")
                print("WARNING: Using pseudo-randomness for password generation is not recommended.")
                config["pseudo_random"] = 1
        common.return_prompt()


def get_config():
    """Fetch existing configuration file or create a new one."""
    try:
        with open("config.json", "r", encoding="utf-8") as config_file:
            config = json.loads(config_file.read())
    except FileNotFoundError:
        # Create new file and write the default configuration to it.
        with open("config.json", "w", encoding="utf-8") as config_file:
            config_file.write("{\"initiate\": 0, " +
                              "\"wordlist\": \"wordlists/english3.txt\", " +
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
                        ["Edit configuration.", mod_config],
                        ["Cross-reference an existing password.", wli.cross_ref],
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
            # Reload config in case of change.
            config = get_config()


if __name__ == "__main__":
    start()

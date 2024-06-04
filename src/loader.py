import os
import time
import subprocess
from UserData import cfg

DATA_FILE = "UserData\data.txt"
CONFIG_FILE = "UserData\cfg.py"

if cfg.LOADER_CFG_TRUE_OR_FALSE == True:
    
    os.system("color E & title Loader.exe & cls")
    
    def update_config(option, value):
        with open(CONFIG_FILE, "r") as file:
            lines = file.readlines()

        with open(CONFIG_FILE, "w") as file:
            for line in lines:
                if line.startswith(option):
                    file.write(f"{option} = {value}\n")
                else:
                    file.write(line)

    def load_config(option):
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                if line.startswith(option):
                    return line.split("=")[1].strip() == "1"
        return 0

    def get_username():
        if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
            username = input("Please enter your username: ")
            with open(DATA_FILE, "w") as file:
                file.write(username)
        else:
            with open(DATA_FILE, "r") as file:
                username = file.read().strip()
        return username

    def main_menu():
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("If Anonim tool is not functioning properly, your first step should be to run this script with administrative privileges.")
            print("\nPlease choose an option:")
            print("[1] Start installing library")
            print("[2] Start Anonim tool")
            print("[3] Settings")
            print("[4] Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                install_libraries()
            elif choice == "2":
                start_anonim_tool()
            elif choice == "3":
                print("Sorry, this available only for administrator, you are not administrator :( ")
                time.sleep(2)

            elif choice == "4":
                exit_program()
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

    def install_libraries():
        os.system("cls" if os.name == "nt" else "clear")
        print("\nThis can take up to 5 minutes...")
        time.sleep(2)
        subprocess.run(["pip", "install", "--upgrade", "pip"])
        subprocess.run(["pip", "install", "-r", "lib.txt"])
        os.system("cls" if os.name == "nt" else "clear")
        print("Successfully installed libraries.")
        input("Press Enter to continue...")

    def start_anonim_tool():
        os.system("cls" if os.name == "nt" else "clear")
        print("Loading...")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print("Starting Anonim tool...")
        os.system("cd Process & start Process.exe")
            
        input("Press Enter to continue...")
    
    def settings_menu():
        os.system("start settings_app.exe")

    def exit_program():
        os.system("cls" if os.name == "nt" else "clear")
        print("Exiting...")
        time.sleep(1)
        exit()

    if __name__ == "__main__":
        username = get_username()
        print(f"Hello, {username}!")
        time.sleep(2)
        main_menu()
else:
    os.system("cd Process & start Process.exe")

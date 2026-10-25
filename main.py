import os
from datetime import datetime

from users import *
from filesystem import *
from processes import *
from memory import *

OS_NAME = "MiniOS ITBOYS SC1064"
VERSION = "1.0"


while not login():
    pass


print("\nWelcome to MiniOS ITBOYS !")

while True:

    command = input("\nMiniOS> ").split()

    if len(command) == 0:
        continue

    cmd = command[0].lower()

    # GENERAL COMMANDS

    if cmd == "help":

        print("""
Available Commands

help
clear
date
time
whoami
systeminfo
exit

File Management
dir
mkdir
create
read
delete

Process Management
process
run
kill

Memory Management
memory
allocate
free
        """)

    elif cmd == "clear":
        os.system("cls")

    elif cmd == "date":
        print(datetime.now().date())

    elif cmd == "time":
        print(datetime.now().strftime("%H:%M:%S"))

    elif cmd == "whoami":
        whoami()

    elif cmd == "systeminfo":

        print("=" * 40)
        print("SYSTEM INFORMATION")
        print("=" * 40)

        print(f"OS Name: {OS_NAME}")
        print(f"Version: {VERSION}")
        print("Architecture: 64-bit")
        print("CPU: Virtual CPU")
        print("Memory: 1024 MB")
        print(f"User: {current_user}")

    elif cmd == "exit":

        print("Shutting down MiniOS...")
        print("Goodbye!")
        break

    # FILE COMMANDS

    elif cmd == "dir":
        dir_command()

    elif cmd == "mkdir":

        if len(command) < 2:
            print("Usage: mkdir <folder>")
        else:
            mkdir_command(command[1])

    elif cmd == "create":

        if len(command) < 2:
            print("Usage: create <filename>")
        else:
            create_file(command[1])

    elif cmd == "read":

        if len(command) < 2:
            print("Usage: read <filename>")
        else:
            read_file(command[1])

    elif cmd == "delete":

        if len(command) < 2:
            print("Usage: delete <filename>")
        else:
            delete_file(command[1])

    # PROCESS COMMANDS

    elif cmd == "process":
        list_processes()

    elif cmd == "run":

        if len(command) < 2:
            print("Usage: run <process_name>")
        else:
            run_process(command[1])

    elif cmd == "kill":

        if len(command) < 2:
            print("Usage: kill <pid>")
        else:
            kill_process(int(command[1]))

    # MEMORY COMMANDS

    elif cmd == "memory":
        memory_status()

    elif cmd == "allocate":

        if len(command) < 2:
            print("Usage: allocate <size>")
        else:
            allocate(int(command[1]))

    elif cmd == "free":

        if len(command) < 2:
            print("Usage: free <size>")
        else:
            free_memory(int(command[1]))

    else:
        print("Unknown command.")
        print("Type 'help' to see available commands.")
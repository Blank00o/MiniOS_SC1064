import os

ROOT = "virtual_disk"

if not os.path.exists(ROOT):
    os.mkdir(ROOT)


def dir_command():
    files = os.listdir(ROOT)

    if len(files) == 0:
        print("Directory empty.")
        return

    for item in files:
        print(item)


def mkdir_command(folder):
    path = os.path.join(ROOT, folder)

    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory created.")
    else:
        print("Folder already exists.")


def create_file(filename):
    path = os.path.join(ROOT, filename)

    with open(path, "w") as file:
        content = input("Enter file content: ")
        file.write(content)

    print("File created.")


def read_file(filename):
    try:
        path = os.path.join(ROOT, filename)

        with open(path, "r") as file:
            print(file.read())
    except:
        print("Error: File does not exist.")


def delete_file(filename):
    try:
        os.remove(os.path.join(ROOT, filename))
        print("File deleted.")
    except:
        print("Error: File does not exist.")
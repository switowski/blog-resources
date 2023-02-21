import os
import glob
from pathlib import Path


# Construct some dummy path
def os_path_join():
    return os.path.join("/", "some", "nested", "path", "to", "a", "file.txt")


def pathlib_join():
    return Path("/") / "some" / "nested" / "path" / "to" / "a" / "file.txt"


# Same as before but with existing Path object
ROOT = Path("/")


def pathlib_join_existing_object(root=ROOT):
    return root / "some" / "nested" / "path" / "to" / "a" / "file.txt"


# Construct dummy path starting at the home folder for the current user
def os_path_join_home():
    return os.path.join(os.path.expanduser("~"), "some", "nested", "path", "to", "a", "file.txt")


def pathlib_join_home():
    return Path.home() / "some" / "nested" / "path" / "to" / "a" / "file.txt"


# Is it a file?
def os_isfile(name):
    return os.path.isfile(f"./{name}")


def pathlib_is_file(name):
    return Path(f"./{name}").is_file()


# Find all files matching a pattern
def os_walk_files():
    python_files = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".py"):
                python_files.append(f"{root}/{filename}")
    return python_files


def glob_find_files():
    return glob.glob("./**/*.py", recursive=True)


def path_find_files():
    return list(Path().rglob("*.py"))


# Write to a file
def classic_write():
    with open("a_file.txt", "w") as f:
        f.write("hello there")


def pathlib_write():
    Path("a_file.txt").write_text("hello there")

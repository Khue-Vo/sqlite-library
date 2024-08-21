"""CLI To-Do entry point script"""
# __main__.py

from library import lib, __app_name__


def main():
    lib.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()

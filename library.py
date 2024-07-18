"""CLI To-Do entry point script"""
#__main__.py

from database import DatabaseHandler

def main():
    database = DatabaseHandler()
    database.init_database()
    database.add_category('Shop')

if __name__ == "__main__":
    main()

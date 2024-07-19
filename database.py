"""This module provides the library database functionality."""

import sqlite3
import os

my_library = 'library.db'
conn = sqlite3.connect(my_library)
conn.close()

class DatabaseHandler:

    def __init__(self):
        print("Initialize database...")
        self._conn = conn
        lib_path = os.path.abspath(my_library)
        print(f"The database is {lib_path}")
        self._conn.close()

    def init_table(self):
        try:
            # Initialize tables
            conn.execute('''CREATE TABLE IF NOT EXISTS Genre
                            (Genre_ID INTEGER NOT NULL,
                             GenreName TEXT UNIQUE,
                             PRIMARY KEY(Genre_ID AUTOINCREMENT)
                             );''')
            conn.execute('''CREATE TABLE IF NOT EXISTS Author
                            (Author_ID	INTEGER NOT NULL,
                            FirstName	TEXT,
                            LastName	TEXT,
                            Birthday	TEXT,
                            PRIMARY KEY(Author_ID AUTOINCREMENT)
                            );''')
            conn.execute('''CREATE TABLE IF NOT EXISTS Book
                            (Book_ID INTEGER NOT NULL,
                            Title TEXT UNIQUE,
                            Genre_ID INTEGER,
                            Series TEXT,
                            Author_ID INTEGER,
                            LoanStatus TEXT DEFAULT 'Available',                            
                            FOREIGN KEY(Author_ID) REFERENCES Author(Author_ID)
                            FOREIGN KEY(Genre_ID) REFERENCES Genre(Genre_ID),
                            PRIMARY KEY(Book_ID AUTOINCREMENT)
                            );''')
            conn.execute('''CREATE TABLE IF NOT EXISTS User
                            (User_ID INTEGER NOT NULL,
                            FirstName TEXT,
                            LastName TEXT,
                            Address TEXT,
                            Email TEXT UNIQUE,
                            PhoneNumber TEXT UNIQUE,
                            PRIMARY KEY(User_ID AUTOINCREMENT)
                            );''')
            conn.execute('''CREATE TABLE IF NOT EXISTS Loan
                            (Loan_ID INTEGER NOT NULL,
                            Book_ID INTEGER,
                            User_ID INTEGER,
                            LoanDay TEXT DEFAULT CURRENT_DATE,
                            ReturnDay TEXT,
                            FOREIGN KEY(Book_ID) REFERENCES Book(Book_ID),
                            FOREIGN KEY(User_ID) REFERENCES User(User_ID),
                            PRIMARY KEY(Loan_ID AUTOINCREMENT)
                            );''')
            print("Tables created successfully.")
            conn.close()
        except sqlite3.Error as e:
            return e


    def add_genre(self, genre: str):
        try:
            conn = sqlite3.connect(my_library)
            print('add_category')

        except sqlite3.Error as e:
            return e

    # def remove_genre(self, genreName: str):
    #     print("Genre removed successfully.")
    #
    # def update_genre(self, genreID: int):
    #     print("Genre updated successfully.")
    #
    # def add_author(self, author: str):
    #     print("Author added successfully.")
    #
    # def remove_author(self, authorName: str):
    #     print("Author removed successfully.")
    #
    # def update_author(self, authorID: int):
    #     print("Author updated successfully.")
    #
    # def add_book(self, book_name: str, category_id: int):
    #     print('add_book')
    #
    # def remove_book(self, bookTitle: str):
    #     print("Book removed successfully.")
    #
    # def update_book(self, bookID: int):
    #     print("Book updated successfully.")
    #
    # def add_user(self, user: str):
    #     print("User added successfully.")
    #
    # def remove_user(self, userName: str):
    #     print("User removed successfully.")
    #
    # def update_user(self, userID: int):
    #     print("User updated successfully.")
    #
    # def add_loan(self, loan: str):
    #     print("Loan added successfully.")
    #
    # def remove_loan(self, loanID: int):
    #     print("Loan removed successfully.")
    #
    # def update_loan(self, loanID: int):
    #     print("Loan updated successfully.")

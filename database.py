"""This module provides the library database functionality."""

import sqlite3
import os

from typing import List

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
            self._conn = conn
            # Initialize tables
            self._conn.execute('''CREATE TABLE IF NOT EXISTS Genre
                            (Genre_ID INTEGER NOT NULL,
                             GenreName TEXT UNIQUE,
                             PRIMARY KEY(Genre_ID AUTOINCREMENT)
                             );''')
            self._conn.execute('''CREATE TABLE IF NOT EXISTS Author
                            (Author_ID	INTEGER NOT NULL,
                            FirstName	TEXT,
                            LastName	TEXT,
                            Birthday	TEXT,
                            PRIMARY KEY(Author_ID AUTOINCREMENT)
                            );''')
            self._conn.execute('''CREATE TABLE IF NOT EXISTS Book
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
            self._conn.execute('''CREATE TABLE IF NOT EXISTS User
                            (User_ID INTEGER NOT NULL,
                            FirstName TEXT,
                            LastName TEXT,
                            Address TEXT,
                            Email TEXT UNIQUE,
                            PhoneNumber TEXT UNIQUE,
                            PRIMARY KEY(User_ID AUTOINCREMENT)
                            );''')
            self._conn.execute('''CREATE TABLE IF NOT EXISTS Loan
                            (Loan_ID INTEGER NOT NULL,
                            Book_ID INTEGER,
                            User_ID INTEGER,
                            LoanDay TEXT DEFAULT CURRENT_DATE,
                            ReturnDay TEXT,
                            FOREIGN KEY(Book_ID) REFERENCES Book(Book_ID),
                            FOREIGN KEY(User_ID) REFERENCES User(User_ID),
                            PRIMARY KEY(Loan_ID AUTOINCREMENT)
                            );''')
            self._conn.commit()
            print("Tables created successfully.")
            self._conn.close()
        except sqlite3.Error as e:
            return e


    def add_genre(self, genreName: str):
        try:
            self._conn = conn
            self._conn.execute('INSERT INTO Genre (GenreName) VALUES (?)', (genreName,))
            self._conn.commit()
            self._conn.close()
            print(f"Genre '{genreName}' added successfully.")
        except sqlite3.Error as e:
            return e

    def remove_genre(self, genreName: str):
        try:
            self._conn = conn
            self._conn.execute('DELETE FROM Genre WHERE GenreName = ?', (genreName,))
            self._conn.commit()
            self._conn.close()
            print(f"Genre '{genreName}' removed successfully.")
        except sqlite3.Error as e:
            return e


    # def update_genre(self, genreID: int):
    #     print("Genre updated successfully.")
    #
    def add_author(self, author: List[str], birth: str):
        try:
            self._conn = conn
            self._conn.execute('INSERT INTO Author (FirstName, LastName, Birthday) VALUES (?,?,?)', (author[0], author[1], birth,))
            self._conn.commit()
            self._conn.close()
            fullname = " ".join(author)
            print(f"Author '{fullname}' added successfully.")
        except sqlite3.Error as e:
            return e

    def remove_author(self, author: List[str]):
        try:
            self._conn = conn
            self._conn.execute('DELETE FROM Author WHERE FirstName = ? AND LastName = ?', (author[0], author[1],))
            self._conn.commit()
            self._conn.close()
            fullname = " ".join(author)
            print(f"Author '{fullname}' removed successfully.")
        except sqlite3.Error as e:
            return e

    # def update_author(self, authorID: int):
    #     print("Author updated successfully.")
    #
    def add_book(self, book_title: str, genre_id: int, series: str, author_id: int):
        try:
            self._conn = conn
            self._conn.execute('INSERT INTO Book (Title, Genre_ID, Series, Author_ID) VALUES (?,?,?,?)', (book_title, genre_id, series, author_id,))
            self._conn.commit()
            self._conn.close()
            print(f"Book '{book_title}' added successfully.")
        except sqlite3.Error as e:
            return e

    def remove_book(self, bookTitle: str):
        try:
            self._conn = conn
            self._conn.execute('DELETE FROM Book WHERE Title = ?', (bookTitle,))
            self._conn.commit()
            self._conn.close()
            print(f"Book '{bookTitle}' removed successfully.")
        except sqlite3.Error as e:
            return e

    # def update_book(self, bookID: int):
    #     print("Book updated successfully.")
    #
    def add_user(self, userName: List[str], address: str, email: str, phone_num: str):
        try:
            self._conn = conn
            self._conn.execute('INSERT INTO User (FirstName, LastName, Address, Email, PhoneNumber) VALUES (?,?,?,?,?)', (userName[0], userName[1], address, email, phone_num,))
            self._conn.commit()
            self._conn.close()
            fullname = " ".join(userName)
            print(f"User '{fullname}' added successfully.")
        except sqlite3.Error as e:
            return e

    def remove_user(self, userName: List[str]):
        try:
            self._conn = conn
            self._conn.execute('DELETE FROM User WHERE FirstName = ? AND LastName = ?', (userName[0], userName[1],))
            self._conn.commit()
            self._conn.close()
            fullname = " ".join(userName)
            print(f"User '{fullname}' removed successfully.")
        except sqlite3.Error as e:
            return e

    # def update_user(self, userID: int):
    #     print("User updated successfully.")
    #
    def add_loan(self, book_id: int, user_id: int, return_day: str):
        try:
            self._conn = conn
            self._conn.execute('INSERT INTO Loan (Book_ID, User_ID, ReturnDay) VALUES (?,?,?)', (book_id, user_id, return_day,))
            self._conn.commit()
            self._conn.close()
            print(f"Loan added successfully.")
        except sqlite3.Error as e:
            return e

    def remove_loan(self, loanID: int):
        print("Loan removed successfully.")

    # def update_loan(self, loanID: int):
    #     print("Loan updated successfully.")

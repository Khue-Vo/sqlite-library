"""This module provides the library database functionality."""
# database.py


import sqlite3
from typing import List

import typer


class DatabaseHandler:
    my_library = 'library.db'

    def __init__(self):
        try:
            self._conn = sqlite3.connect(self.my_library)
        except sqlite3.Error as e:
            typer.secho(f"Error while creating database: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def init_table(self):
        try:
            """Initialize tables."""
            with self._conn:
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
                                LoanDate TEXT DEFAULT CURRENT_DATE,
                                DueDate INTEGER, DateReturn INTEGER,
                                LoanStatus TEXT DEFAULT "Not Return",
                                FOREIGN KEY(Book_ID) REFERENCES Book(Book_ID),
                                FOREIGN KEY(User_ID) REFERENCES User(User_ID),
                                PRIMARY KEY(Loan_ID AUTOINCREMENT)
                                );''')
                self._conn.execute('''CREATE TRIGGER IF NOT EXISTS update_book_status
                                AFTER INSERT ON Loan
                                FOR EACH ROW
                                BEGIN
                                    UPDATE Book
                                    SET LoanStatus = 'Not Available'
                                    WHERE Book_ID = NEW.Book_ID;
                                END''')
                self._conn.execute('''CREATE TRIGGER IF NOT EXISTS update_book_status_return
                                AFTER UPDATE OF LoanStatus ON Loan
                                FOR EACH ROW
                                BEGIN
                                    UPDATE Book
                                    SET LoanStatus = 'Available'
                                    WHERE Book_ID = OLD.Book_ID;
                                END''')
        except sqlite3.Error as e:
            typer.secho(f"Error while creating tables: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def rollback(self):
        try:
            with self._conn:
                self._conn.rollback()
        except sqlite3.Error as e:
            typer.secho(f"Error: {e}.", fg=typer.colors.RED)
            raise typer.Exit()

    def add_genre(self, genre_name: str):
        try:
            with self._conn:
                self._conn.execute('INSERT INTO Genre (GenreName) VALUES (?)',
                                   (genre_name,))
                self._conn.commit()
        except sqlite3.Error as e:
            self.rollback()
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_author(self, first_name: str, last_name: str, birth: str):
        try:
            with self._conn:
                self._conn.execute('INSERT INTO Author (FirstName, LastName, Birthday) VALUES (?,?,?)',
                                   (first_name, last_name, birth,))
                self._conn.commit()
        except sqlite3.Error as e:
            self.rollback()
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_book(self, book_title: str, genre_id: int, series: str, author_id: int):
        try:
            with self._conn:
                self._conn.execute('INSERT INTO Book (Title, Genre_ID, Series, Author_ID) VALUES (?,?,?,?)',
                                   (book_title, genre_id, series, author_id,))
                self._conn.commit()
        except sqlite3.Error as e:
            self.rollback()
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_user(self, first_name: str, last_name: str, address: str, email: str, phone_num: str):
        try:
            with self._conn:
                self._conn.execute(
                    'INSERT INTO User (FirstName, LastName, Address, Email, PhoneNumber) VALUES (?,?,?,?,?)',
                    (first_name, last_name, address, email, phone_num,)
                )
                self._conn.commit()
        except sqlite3.Error as e:
            self.rollback()
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_loan(self, book_id: int, user_id: int, loan_day: str, due_day: str):
        try:
            with self._conn:
                query = 'INSERT INTO Loan (Book_ID, User_ID, LoanDate, DueDate) VALUES (?,?,?,?)'
                params = (book_id, user_id, loan_day, due_day)
                self._conn.execute(query, params)
                self._conn.commit()
        except sqlite3.Error as e:
            self.rollback()
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def update_genre(self, genre_id: int, new_info: str):
        try:
            with self._conn:
                self._conn.execute('''UPDATE Genre SET GenreName = ? WHERE Genre_ID = ?''', (new_info, genre_id))
                self._conn.commit()
        except sqlite3.Error as e:
            self.rollback()
            typer.secho(f"Error while updating information: {e}", fg=typer.colors.RED)
            raise typer.Exit()


#     def list_all_genre(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('SELECT * FROM Genre')
#                 all_genre = cursor.fetchall()
#                 return all_genre
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def list_all_author(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('SELECT * FROM Author')
#                 all_author = cursor.fetchall()
#                 return all_author
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def list_all_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''
#                                 SELECT Book_ID, Title, Series, FirstName, LastName, GenreName
#                                 FROM Book
#                                 INNER JOIN Author ON Book.Author_ID = Author.Author_ID
#                                 INNER JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
#                                 ''')
#                 all_book = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [all_book, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def list_all_user(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('SELECT * FROM User')
#                 all_user = cursor.fetchall()
#                 return all_user
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def list_all_loan(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''
#                                 SELECT Loan_ID, LoanDate, DueDate, Title, FirstName, LastName
#                                 FROM Loan
#                                 INNER JOIN Book ON Loan.Book_ID = Book.Book_ID
#                                 INNER JOIN User ON Loan.User_ID = User.User_ID
#                                 ''')
#                 all_loan = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [all_loan, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_genre_with_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 query = """
#                             SELECT Genre.GenreName, COUNT(Book.Book_ID) AS BookCount
#                             FROM Book
#                             INNER JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
#                             GROUP BY Genre.GenreName
#                             ORDER BY BookCount DESC
#                             LIMIT 1
#                         """
#                 cursor.execute(query)
#                 genre_max = cursor.fetchall()
#                 query = """
#                             SELECT Genre.Genre_ID, GenreName, Title
#                             FROM Genre
#                             INNER JOIN Book ON Genre.Genre_ID = Book.Genre_ID
#                             WHERE GenreName = ?
#                         """
#                 cursor.execute(query, (genre_max[0][0],))
#                 author_with_book = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [genre_max, author_with_book, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_author_with_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 query = """
#                             SELECT Author.FirstName, Author.LastName, COUNT(Book.Book_ID) AS BookCount
#                             FROM Book
#                             INNER JOIN Author ON Book.Author_ID = Author.Author_ID
#                             GROUP BY Author.Author_ID, Author.FirstName, Author.LastName
#                             ORDER BY BookCount DESC
#                             LIMIT 1
#                         """
#                 cursor.execute(query)
#                 author_max = cursor.fetchall()
#                 query = """
#                             SELECT Author.Author_ID, FirstName, LastName, Title
#                             FROM Author
#                             INNER JOIN Book ON Author.Author_ID = Book.Author_ID
#                             WHERE Author.FirstName = ? AND Author.LastName = ?
#
#                         """
#                 cursor.execute(query, (author_max[0][0], author_max[0][1],))
#                 author_with_book = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [author_max, author_with_book, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_series_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Book_ID, Title, Series
#                                 FROM Book
#                                 WHERE Series IS NOT NULL''')
#                 book_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [book_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_non_series_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Book_ID, Title, Series
#                                 FROM Book
#                                 WHERE Series IS NULL''')
#                 book_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [book_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_available_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Book_ID, Title
#                                 FROM Book
#                                 WHERE Book.LoanStatus = "Available"''')
#                 book_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [book_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_non_available_book(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Book_ID, Title
#                                 FROM Book
#                                 WHERE Book.LoanStatus = "Not Available"''')
#                 book_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [book_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def check_if_available(self, book_title):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('SELECT LoanStatus FROM Book WHERE Title = ?', (book_title,))
#                 status = cursor.fetchone()
#                 return status
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_user_with_loan(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Loan.Loan_ID, User.FirstName, LastName, Book.Title FROM Loan
#                                 INNER JOIN User ON Loan.User_ID = User.User_ID
#                                 INNER JOIN Book ON Loan.Book_ID = Book.Book_ID
#                                 WHERE Loan.LoanStatus = "Not Return" ''')
#                 user_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [user_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_returned_loan(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Loan_ID, FirstName, LastName, Title, DateReturn, DueDate FROM Loan
#                                 INNER JOIN Book ON Loan.Book_ID = Book.Book_ID
#                                 INNER JOIN User ON Loan.User_ID = User.User_ID
#                                 WHERE Loan.LoanStatus = "Returned"''')
#                 user_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [user_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def get_overdue_loan(self):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Loan.Loan_ID, User.FirstName, User.LastName, Book.Title, Loan.LoanDate,
#                                 Loan.DueDate, Loan.LoanStatus
#                                 FROM Loan
#                                 INNER JOIN User ON Loan.User_ID = User.User_ID
#                                 INNER JOIN Book ON Loan.Book_ID = Book.Book_ID
#                                 WHERE Loan.LoanStatus = "Not Return" AND Loan.DueDate < CURRENT_DATE''')
#                 loan_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [loan_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_genre(self, genre_name: str):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT GenreName FROM Genre WHERE GenreName = ?''', (genre_name,))
#                 if_exist = cursor.fetchone()
#                 return if_exist
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_author(self, first_name: str, last_name: str):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT FirstName, LastName FROM Author WHERE FirstName = ? AND LastName = ?''',
#                                (first_name, last_name,))
#                 if_exist = cursor.fetchone()
#                 return if_exist
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_book(self, book_title: str):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Title FROM Book WHERE Title = ?''', (book_title,))
#                 if_exist = cursor.fetchone()
#                 return if_exist
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_user(self, first_name: str, last_name: str):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT FirstName, LastName FROM User WHERE FirstName = ? AND LastName = ?''',
#                                (first_name, last_name,))
#                 if_exist = cursor.fetchone()
#                 return if_exist
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_loan(self, user_id: int, book_id: int):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT *  FROM Loan WHERE User_ID = ? AND Book_ID = ?''',
#                                (user_id, book_id,))
#                 if_exist = cursor.fetchone()
#                 return if_exist
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_book_by_genre(self, genre_id: int):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Book.Book_ID, Book.Title, Book.Series, Genre.GenreName,
#                                 Author.FirstName, Author.LastName, Book.LoanStatus
#                                 FROM Book
#                                 INNER JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
#                                 INNER JOIN Author ON Book.Author_ID = Author.Author_ID
#                                 WHERE Book.Genre_ID = ?''',
#                                (genre_id,))
#                 book_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [book_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
#     def search_book_by_author(self, author_id: int):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute('''SELECT Book.Book_ID, Book.Title, Book.Series, Genre.GenreName,
#                                 Author.FirstName, Author.LastName, Book.LoanStatus
#                                 FROM Book
#                                 INNER JOIN Genre ON Book.Genre_ID = Genre.Genre_ID
#                                 INNER JOIN Author ON Book.Author_ID = Author.Author_ID
#                                 WHERE Book.Author_ID = ?''',
#                                (author_id,))
#                 book_list = cursor.fetchall()
#                 column_names = [description[0] for description in cursor.description]
#                 return [book_list, column_names]
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
#             raise typer.Exit()
#
    def get_genre_id(self, genre_name: str):
        try:
            with self._conn:
                cursor = self._conn.cursor()
                cursor.execute('SELECT Genre_ID FROM Genre WHERE GenreName = ?', (genre_name,))
                genre_id = cursor.fetchone()
                return genre_id
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def get_author_id(self, first_name: str, last_name: str):
        try:
            with self._conn:
                cursor = self._conn.cursor()
                cursor.execute('SELECT Author_ID FROM Author WHERE FirstName = ? AND LastName = ?',
                               (first_name, last_name,))
                author_id = cursor.fetchone()
                return author_id
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def get_book_id(self, book_title: str):
        try:
            with self._conn:
                cursor = self._conn.cursor()
                cursor.execute('SELECT Book_ID FROM Book WHERE Title = ?', (book_title,))
                book_id = cursor.fetchone()
                return book_id
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def get_user_id(self, first_name: str, last_name: str):
        try:
            with self._conn:
                cursor = self._conn.cursor()
                query = 'SELECT User_ID FROM User WHERE FirstName = ? AND LastName = ?'
                params = (first_name, last_name)
                cursor.execute(query, params)
                user_id = cursor.fetchone()
                return user_id
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking id: {e}", fg=typer.colors.RED)
            raise typer.Exit()
#
#     def get_columns_name(self, table_name: str):
#         try:
#             with self._conn:
#                 cursor = self._conn.cursor()
#                 cursor.execute(f"PRAGMA table_info({table_name})")
#                 columns = cursor.fetchall()
#                 column_names = [column[1] for column in columns]
#                 return column_names
#         except sqlite3.Error as e:
#             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
#             raise typer.Exit()

"""This module provides the to-do model-controller."""
# library.py

import sqlite3
from typing import List

import typer

from library.database import DatabaseHandler


class Library:
    def __init__(self):
        try:
            self._dbhandler = DatabaseHandler()
            self._dbhandler.init_table()
        except sqlite3.Error as e:
            typer.secho(f"Error while connecting to database: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_genre(self, genre: str):
        try:
            self._dbhandler.add_genre(genre)
        except sqlite3.Error as e:
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_author(self, first_name: str, last_name: str, birthday: str):
        try:
            self._dbhandler.add_author(first_name, last_name, birthday)
        except sqlite3.Error as e:
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_book(self, book_title: str, genre: str, series: str, author: str):
        try:
            genre_id = self.get_genre_id(genre)
            first_name, last_name = author.split(maxsplit=1)
            author_id = self.get_author_id(first_name, last_name)
            self._dbhandler.add_book(book_title, genre_id, series, author_id)
        except sqlite3.Error as e:
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_user(self, first_name: str, last_name: str, address: str, email: str, phone_num: str):
        try:
            self._dbhandler.add_user(first_name, last_name, address, email, phone_num)
        except sqlite3.Error as e:
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def add_loan(self, book_title: str, user: str, loan_day: str, due_day: str):
        try:
            book_id = self.get_book_id(book_title)
            first_name, last_name = user.split(maxsplit=1)
            user_id = self.get_user_id(first_name, last_name)
            self._dbhandler.add_loan(book_id, user_id, loan_day, due_day)
        except sqlite3.Error as e:
            typer.secho(f"Error while adding information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def update_genre(self, genre_id: int, new_genre: str):
        try:
            self._dbhandler.update_genre(genre_id, new_genre)
        except sqlite3.Error as e:
            typer.secho(f"Error while updating information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def update_author(self, author_id: int, new_name: str, new_birthday: str):
        try:
            if new_name == "null" or new_name == "Null" or new_name == "none" or new_name == "None":
                new_firstname = "null"
                new_lastname = "null"
            else:
                new_firstname, new_lastname = new_name.split(maxsplit=1)
            if new_birthday == "null" or new_birthday == "Null" or new_birthday == "none" or new_birthday == "None":
                new_birthday = "null"
            self._dbhandler.update_author(author_id, new_firstname, new_lastname, new_birthday)
        except sqlite3.Error as e:
            typer.secho(f"Error while updating information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def update_book(self, book_id: int, new_title: str, new_genre: str, new_series: str, new_author: str,
                    new_status: str):
        try:
            if new_title == "null" or new_title == "Null" or new_title == "none" or new_title == "None":
                new_title = "null"

            if new_genre == "null" or new_genre == "Null" or new_genre == "none" or new_genre == "None":
                new_genre_id = 0
            else:
                new_genre_id = self.get_genre_id(new_genre)

            if new_series == "null" or new_series == "Null" or new_series == "none" or new_series == "None":
                new_series = "null"

            if new_author == "null" or new_author == "Null" or new_author == "none" or new_author == "None":
                new_author_id = 0
            else:
                first_name, last_name = new_author.split(maxsplit=1)
                new_author_id = self.get_author_id(first_name, last_name)

            if new_status == "null" or new_status == "Null" or new_status == "none" or new_status == "None":
                new_status = "null"

            self._dbhandler.update_book(book_id, new_title, new_genre_id, new_series, new_author_id, new_status)
        except sqlite3.Error as e:
            typer.secho(f"Error while updating information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def update_user(self, user_id: int, new_name: str, new_address: str, new_email: str, new_phone: str):
        try:
            if new_name == "null" or new_name == "Null" or new_name == "none" or new_name == "None":
                new_firstname = "null"
                new_lastname = "null"
            else:
                new_firstname, new_lastname = new_name.split(maxsplit=1)

            if new_address == "null" or new_address == "Null" or new_address == "none" or new_address == "None":
                new_address = "null"

            if new_email == "null" or new_email == "Null" or new_email == "none" or new_email == "None":
                new_email = "null"

            if new_phone == "null" or new_phone == "Null" or new_phone == "none" or new_phone == "None":
                new_phone = "null"

            self._dbhandler.update_user(user_id, new_firstname, new_lastname, new_address, new_email, new_phone)
        except sqlite3.Error as e:
            typer.secho(f"Error while updating information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def update_loan(self, loan_id: int, new_book: str, new_user: str, new_loandate: str, new_duedate: str,
                    new_returndate: str, new_loanstatus: str):
        try:
            if new_book == "null" or new_book == "Null" or new_book == "none" or new_book == "None":
                new_book_id = 0
            else:
                new_book_id = self.get_book_id(new_book)

            if new_user == "null" or new_user == "Null" or new_user == "none" or new_user == "None":
                new_user_id = 0
            else:
                new_user_id = self.get_book_id(new_book)

            if new_loandate == "null" or new_loandate == "Null" or new_loandate == "none" or new_loandate == "None":
                new_loandate = "null"

            if new_duedate == "null" or new_duedate == "Null" or new_duedate == "none" or new_duedate == "None":
                new_duedate = "null"

            if new_returndate == "null" or new_returndate == "Null" or new_returndate == "none" or new_returndate == "None":
                new_returndate = "null"

            if new_loanstatus == "null" or new_loanstatus == "Null" or new_loanstatus == "none" or new_loanstatus == "None":
                new_loanstatus = "null"

            self._dbhandler.update_loan(loan_id, new_book_id, new_user_id, new_loandate, new_duedate, new_returndate,
                                        new_loanstatus)
        except sqlite3.Error as e:
            typer.secho(f"Error while updating information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def list_all_genre(self):
        try:
            all_genre = self._dbhandler.list_all_genre()
            column_names = self._dbhandler.get_columns_name("Genre")
            return [all_genre, column_names]
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

        def list_all_author(self):
            try:
                all_author = self._dbhandler.list_all_author()
                column_names = self._dbhandler.get_columns_name("Author")
                return [all_author, column_names]
            except sqlite3.Error as e:
                typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
                raise typer.Exit()

    #     def list_all_book(self):
    #         try:
    #             all_book, column_names = self._dbhandler.list_all_book()
    #             return [all_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def list_all_user(self):
    #         try:
    #             all_user = self._dbhandler.list_all_user()
    #             column_names = self._dbhandler.get_columns_name("User")
    #             return [all_user, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def list_all_loan(self):
    #         try:
    #             all_loan, column_names = self._dbhandler.list_all_loan()
    #             return [all_loan, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def genre_with_most_book(self):
    #         try:
    #             genre_max, genre_with_book, column_names = self._dbhandler.get_genre_with_book()
    #             genre_name = genre_max[0][0]
    #             book_number = genre_max[0][1]
    #             return [genre_name, book_number, genre_with_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def author_with_most_book(self):
    #         try:
    #             author_max, author_with_book, column_names = self._dbhandler.get_author_with_book()
    #             author_name = author_max[0][0] + " " + author_max[0][1]
    #             book_number = author_max[0][2]
    #             return [author_name, book_number, author_with_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def book_in_series(self):
    #         try:
    #             series_book, column_names = self._dbhandler.get_series_book()
    #             return [series_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def book_not_in_series(self):
    #         try:
    #             non_series_book, column_names = self._dbhandler.get_non_series_book()
    #             return [non_series_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def available_books_for_loan(self):
    #         try:
    #             available_book, column_names = self._dbhandler.get_available_book()
    #             return [available_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def non_available_books_for_loan(self):
    #         try:
    #             non_available_book, column_names = self._dbhandler.get_non_available_book()
    #             return [non_available_book, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def check_if_available(self, book_title):
    #         try:
    #             book_status = self._dbhandler.check_if_available(book_title)
    #             return book_status[0]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def user_with_loan(self):
    #         try:
    #             user_list, column_names = self._dbhandler.get_user_with_loan()
    #             return [user_list, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def returned_loan(self):
    #         try:
    #             loan_list, column_names = self._dbhandler.get_returned_loan()
    #             return [loan_list, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def overdue_loan(self):
    #         try:
    #             loan_list, column_names = self._dbhandler.get_overdue_loan()
    #             return [loan_list, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_genre(self, genre_name: str):
    #         try:
    #             genre = self._dbhandler.search_genre(genre_name)
    #             if genre:
    #                 return True
    #             else:
    #                 return False
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_author(self, author_name: str):
    #         try:
    #             first_name, last_name = author_name.split(" ", maxsplit=1)
    #             author = self._dbhandler.search_author(first_name, last_name)
    #             if author:
    #                 return True
    #             else:
    #                 return False
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_book(self, book_title: str):
    #         try:
    #             book = self._dbhandler.search_book(book_title)
    #             if book:
    #                 return True
    #             else:
    #                 return False
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_user(self, user_name):
    #         try:
    #             first_name, last_name = user_name.split(" ", maxsplit=1)
    #             user = self._dbhandler.search_user(first_name, last_name)
    #             if user:
    #                 return True
    #             else:
    #                 return False
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_loan(self, user_name, book_title):
    #         try:
    #             first_name, last_name = user_name.split(" ", maxsplit=1)
    #             user_id = self.get_user_id(first_name, last_name)
    #             book_id = self.get_book_id(book_title)
    #             loan = self._dbhandler.search_loan(user_id, book_id)
    #             if loan:
    #                 return True
    #             else:
    #                 return False
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_book_by_genre(self, genre_name: str):
    #         try:
    #             genre_id = self.get_genre_id(genre_name)
    #             book_list, column_names = self._dbhandler.search_book_by_genre(genre_id)
    #             return [book_list, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()
    #
    #     def search_book_by_author(self, author_name: str):
    #         try:
    #             first_name, last_name = author_name.split(maxsplit=1)
    #             author_id = self.get_author_id(first_name, last_name)
    #             book_list, column_names = self._dbhandler.search_book_by_author(author_id)
    #             return [book_list, column_names]
    #         except sqlite3.Error as e:
    #             typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
    #             raise typer.Exit()

    def get_genre_id(self, genre_name):
        try:
            genre_id = self._dbhandler.get_genre_id(genre_name)
            if genre_id:
                return genre_id[0]
            else:
                typer.secho("Genre doesn't exist. Please enter another genre's name.", fg=typer.colors.RED)
                raise typer.Exit()
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def get_author_id(self, first_name, last_name):
        try:
            author_id = self._dbhandler.get_author_id(first_name, last_name)
            if author_id:
                return author_id[0]
            else:
                typer.secho("Author doesn't exist. Please enter another author's name.", fg=typer.colors.RED)
                raise typer.Exit()
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def get_book_id(self, book_name):
        try:
            book_id = self._dbhandler.get_book_id(book_name)
            if book_id:
                return book_id[0]
            else:
                typer.secho("Book doesn't exist. Please enter another book's title.", fg=typer.colors.RED)
                raise typer.Exit()
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

    def get_user_id(self, first_name, last_name):
        try:
            user_id = self._dbhandler.get_user_id(first_name, last_name)
            if user_id:
                return user_id[0]
            else:
                typer.secho("User doesn't exist. Please enter another user's name.", fg=typer.colors.RED)
                raise typer.Exit()
        except sqlite3.Error as e:
            typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
            raise typer.Exit()

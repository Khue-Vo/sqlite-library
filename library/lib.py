"""This module provides the library management"""
# lib.py

import typer
from typing import Optional
import sqlite3
from library.library import Library
from library import (__version__, __app_name__)

app = typer.Typer()
lib: Optional[Library] = None


def get_database():
    global lib
    lib = Library()


@app.command()
def init() -> None:
    """Initialize the library database."""
    try:
        get_database()
        typer.secho("Initialized the database successfully."
                    "\nThe database is C:\\Users\\Khue Vo\\training\\python\\sqlite-library\\library.db",
                    fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while initializing the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def add_genre(
        genre: str = typer.Option(..., prompt="Genre name"),
) -> None:
    """Add genre information into the library database."""
    try:
        get_database()
        lib.add_genre(genre)
        typer.secho(f"Genre {genre} successfully added.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error adding genre into the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def add_author(
        first_name: str = typer.Option(..., prompt="First name"),
        last_name: str = typer.Option(..., prompt="Last name"),
        birthday: str = typer.Option(..., prompt="Birthday(YYYY-DD-MM)"),
) -> None:
    """Add author information into the library database."""
    try:
        get_database()
        lib.add_author(first_name, last_name, birthday)
        typer.secho(f"Author {first_name} {last_name} added successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error adding author into the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def add_book(
        title: str = typer.Option(..., prompt="Title"),
        genre: str = typer.Option(..., prompt="Genre"),
        series: str = typer.Option(..., prompt="Series"),
        author: str = typer.Option(..., prompt="Author"),
) -> None:
    """Add book information into the library database."""
    try:
        get_database()
        lib.add_book(title, genre, series, author)
        typer.secho(f"Book {title} successfully added.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error adding book into the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def add_user(
        first_name: str = typer.Option(..., prompt="First name"),
        last_name: str = typer.Option(..., prompt="Last name"),
        address: str = typer.Option(..., prompt="Address"),
        email: str = typer.Option(..., prompt="Email"),
        phone: str = typer.Option(..., prompt="Phone Number"),
) -> None:
    """Add user information into the library database."""
    try:
        get_database()
        lib.add_user(first_name, last_name, address, email, phone)
        typer.secho(f"User {first_name} {last_name} added successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error adding user into the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def add_loan(
        title: str = typer.Option(..., prompt="Book Title"),
        user: str = typer.Option(..., prompt="User's Name"),
        loan_day: str = typer.Option(..., prompt="Loan Day"),
        due_day: str = typer.Option(..., prompt="Due Day"),
) -> None:
    """Add loan information into the library database."""
    try:
        get_database()
        lib.add_loan(title, user, loan_day, due_day)
        typer.secho(f"Loan added successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error adding loan into the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def update_genre(genre_id: int = typer.Option(..., prompt="Genre's ID"),
                 info: str = typer.Option(..., prompt="New genre")) -> None:
    """Update the chosen genre information in the library database."""
    try:
        get_database()
        lib.update_genre(genre_id, info)
        typer.secho(f"Genre updated successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while updating genre: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def update_author(author_id: int = typer.Option(..., prompt="Author's ID"),
                  new_name: str = typer.Option(..., prompt="New name"),
                  new_birthday: str = typer.Option(..., prompt="New birthday")) -> None:
    """Update the chosen author information in the library database."""
    try:
        get_database()
        lib.update_author(author_id, new_name, new_birthday)
        typer.secho(f"Author updated successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while updating author: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def update_book(book_id: int = typer.Option(..., prompt="Book's ID"),
                new_title: str = typer.Option(..., prompt="New title"),
                new_genre: str = typer.Option(..., prompt="New genre"),
                new_series: str = typer.Option(..., prompt="New series"),
                new_author: str = typer.Option(..., prompt="New author"),
                new_status: str = typer.Option(..., prompt="New loan status")) -> None:
    """Update the chosen book information in the library database."""
    try:
        get_database()
        lib.update_book(book_id, new_title, new_genre, new_series, new_author, new_status)
        typer.secho(f"Book updated successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while updating book: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def update_user(user_id: int = typer.Option(..., prompt="User's ID"),
                new_name: str = typer.Option(..., prompt="New name"),
                new_address: str = typer.Option(..., prompt="New address"),
                new_email: str = typer.Option(..., prompt="New email"),
                new_phone: str = typer.Option(..., prompt="New phone number")
                ) -> None:
    """Update the chosen user information in the library database."""
    try:
        get_database()
        lib.update_user(user_id, new_name, new_address, new_email, new_phone)
        typer.secho(f"User updated successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while updating user: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def update_loan(loan_id: int = typer.Option(..., prompt="Loan's ID"),
                new_book: str = typer.Option(..., prompt="New book title"),
                new_user: str = typer.Option(..., prompt="New user's name"),
                new_loandate: str = typer.Option(..., prompt="New loan date"),
                new_duedate: str = typer.Option(..., prompt="New due date"),
                new_returndate: str = typer.Option(..., prompt="New return date"),
                new_loanstatus: str = typer.Option(..., prompt="New loan status"), ) -> None:
    """Update the chosen loan information in the library database."""
    try:
        get_database()
        lib.update_loan(loan_id, new_book, new_user, new_loandate, new_duedate, new_returndate, new_loanstatus)
        typer.secho(f"Loan updated successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while updating loan: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def info_genre(genre_id: int = typer.Option(..., prompt="Genre's ID")) -> None:
    """Check a specific genre's information in the library database."""
    try:
        get_database()
        genre, column_names = lib.info_genre(genre_id)
        print_table(f"Genre details:", genre, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def info_author(author_id: int = typer.Option(..., prompt="Author's ID")) -> None:
    """Check a specific author's information in the library database."""
    try:
        get_database()
        author, column_names = lib.info_author(author_id)
        print_table(f"Author details:", author, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def info_book(book_id: int = typer.Option(..., prompt="Book's ID")) -> None:
    """Check a specific book's information in the library database."""
    try:
        get_database()
        book, column_names = lib.info_book(book_id)
        print_table(f"Book details:", book, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def info_user(user_id: int = typer.Option(..., prompt="User's ID")) -> None:
    """Check a specific user's information in the library database."""
    try:
        get_database()
        user, column_names = lib.info_user(user_id)
        print_table(f"User details:", user, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while invoking information: {e}", fg=typer.colors.RED)
        raise typer.Exit()

# def info_loan(loan_id: int = typer.Option(..., prompt="Loan's ID")) -> None:
#     """Check a specific loan's information in the library database."""


@app.command()
def list_all_genre() -> None:
    """Show all genres within the library database."""
    try:
        get_database()
        all_genre, column_name = lib.list_all_genre()
        if len(all_genre) == 0:
            typer.secho("There are no genre in the table yet. Please add one first.", fg=typer.colors.RED)
            raise typer.Exit()
        print_table("Genre", all_genre, column_name)
        typer.secho(f"\nGenre table listed successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing genres from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def list_all_author() -> None:
    """Show all authors within the library database."""
    try:
        get_database()
        all_author, column_name = lib.list_all_author()
        if len(all_author) == 0:
            typer.secho("There are no author in the table yet. Please add one first.", fg=typer.colors.RED)
            raise typer.Exit()
        print_table("Author", all_author, column_name)
        typer.secho(f"\nAuthor table listed successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing authors from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def list_all_book() -> None:
    """Show all books within the library database."""
    try:
        get_database()
        all_book, column_name = lib.list_all_book()
        if len(all_book) == 0:
            typer.secho("There are no book in the table yet. Please add one first.", fg=typer.colors.RED)
            raise typer.Exit()
        print_table("Book", all_book, column_name)
        typer.secho(f"\nBook table listed successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing books from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def list_all_user() -> None:
    """Show all users within the library database."""
    try:
        get_database()
        all_user, column_name = lib.list_all_user()
        if len(all_user) == 0:
            typer.secho("There are no user in the table yet. Please add one first.", fg=typer.colors.RED)
            raise typer.Exit()
        print_table("User", all_user, column_name)
        typer.secho(f"\nUser table listed successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing users from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def list_all_loan() -> None:
    """Show all loans within the library database."""
    try:
        get_database()
        all_loan, column_name = lib.list_all_loan()
        if len(all_loan) == 0:
            typer.secho("There are no loan in the table yet. Please add one first.", fg=typer.colors.RED)
            raise typer.Exit()
        print_table("Loan", all_loan, column_name)
        typer.secho(f"\nLoan table listed successfully.", fg=typer.colors.GREEN)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing loans from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


# @app.command()
# def show_genre_with_most_book() -> None:
#     """Show the genre which have the most books stored in the library database."""
#     try:
#         get_database()
#         genre_name, book_number, genre_with_book, column_names = lib.genre_with_most_book()
#         print_table(f"\nGenre {genre_name} has the most book in the library: {book_number}", genre_with_book,
#                     column_names)
#         typer.secho(f"\nInformation listed successfully.", fg=typer.colors.GREEN)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while listing genre with the most books from the database: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
# @app.command()
# def show_author_with_most_book() -> None:
#     """Show the author which have the most books stored in the library database."""
#     try:
#         get_database()
#         author_name, book_number, author_with_book, column_names = lib.author_with_most_book()
#         print_table(f"\nAuthor {author_name} has the most book in the library: {book_number}", author_with_book,
#                     column_names)
#         typer.secho(f"\nInformation listed successfully.", fg=typer.colors.GREEN)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while listing author with the most books from the database: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
# @app.command()
# def show_book_in_series() -> None:
#     """List the books which belongs to a series in the library database."""
#     try:
#         get_database()
#         series_book, column_names = lib.book_in_series()
#         print_table("Series books", series_book, column_names)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while listing series books from the database: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
# @app.command()
# def show_book_not_in_series() -> None:
#     """List the books which does not belong to a series in the library database."""
#     try:
#         get_database()
#         non_series_book, column_names = lib.book_not_in_series()
#         print_table("Non-series books", non_series_book, column_names)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while listing non-series books from the database: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
@app.command()
def list_available_book() -> None:
    """List the books that are available for loan in the library database."""
    try:
        get_database()
        available_book, column_names = lib.available_books_for_loan()
        print_table("Available book(s) for loan", available_book, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing available books from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def list_non_available_book() -> None:
    """List the books that are not available for loan in the library database."""
    try:
        get_database()
        non_available_book, column_names = lib.non_available_books_for_loan()
        print_table("Non-available book(s) for loan", non_available_book, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while listing non-available books from the database: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


# @app.command()
# def check_available_book(title: str = typer.Option(..., prompt="Title")) -> None:
#     """Check if a specific book is available for loan or not."""
#     try:
#         get_database()
#         book_status = lib.check_if_available(title)
#         if book_status == "Available":
#             typer.secho(f"The book {title} is available for loan.", fg=typer.colors.GREEN)
#         elif book_status == "Not Available":
#             typer.secho(f"The book {title} is unavailable for loan.", fg=typer.colors.RED)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while checking available of book: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
# @app.command()
# def check_user_with_loan() -> None:
#     """Check which user is currently borrowing books from the library."""
#     try:
#         get_database()
#         user_with_loan, column_names = lib.user_with_loan()
#         print_table(f"The users which are currently borrowing books from library:", user_with_loan, column_names)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while checking user's loan status: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
# @app.command()
# def check_returned_loan() -> None:
#     """Check which loan is returned."""
#     try:
#         get_database()
#         loan_list, column_names = lib.returned_loan()
#         print_table("Loans that have been returned.", loan_list, column_names)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
# @app.command()
# def check_overdue_loan() -> None:
#     """Check which loan is overdue."""
#     try:
#         get_database()
#         loan_list, column_names = lib.overdue_loan()
#         print_table("Loans that is overdue.", loan_list, column_names)
#     except sqlite3.Error as e:
#         typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
#         raise typer.Exit()
#
#
@app.command()
def search_genre(genre_name: str = typer.Option(..., prompt="Genre name")) -> None:
    """Search if a specific genre exists in the library database."""
    try:
        get_database()
        exist = lib.search_genre(genre_name)
        if exist:
            typer.secho("Genre does exist.", fg=typer.colors.GREEN)
        else:
            typer.secho("Genre doesn't exist. Please enter another genre's name.", fg=typer.colors.RED)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def search_author(author_name: str = typer.Option(..., prompt="Author name")) -> None:
    """Search if a specific author exists in the library database."""
    try:
        get_database()
        exist = lib.search_author(author_name)
        if exist:
            typer.secho("Author does exist.", fg=typer.colors.GREEN)
        else:
            typer.secho("Author doesn't exist. Please enter another author's name.", fg=typer.colors.RED)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def search_book(book_title: str = typer.Option(..., prompt="Book title")) -> None:
    """Search if a specific book exists in the library database."""
    try:
        get_database()
        exist = lib.search_book(book_title)
        if exist:
            typer.secho("Book does exist.", fg=typer.colors.GREEN)
        else:
            typer.secho("Book doesn't exist. Please enter another book's title.", fg=typer.colors.RED)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def search_user(user_name: str = typer.Option(..., prompt="User's name")) -> None:
    """Search if a specific user exists in the library database."""
    try:
        get_database()
        exist = lib.search_user(user_name)
        if exist:
            typer.secho("User does exist.", fg=typer.colors.GREEN)
        else:
            typer.secho("User doesn't exist. Please enter another user's name.", fg=typer.colors.RED)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def search_loan(user_name: str = typer.Option(..., prompt="User's name"),
                book_title: str = typer.Option(..., prompt="Book's title")) -> None:
    """Search if a specific loan exists in the library database."""
    try:
        get_database()
        exist = lib.search_loan(user_name, book_title)
        if exist:
            typer.secho("Loan does exist.", fg=typer.colors.GREEN)
        else:
            typer.secho("Loan doesn't exist. Please enter another loan's information.", fg=typer.colors.RED)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def search_by_genre(genre: str = typer.Option(..., prompt="Genre's name")) -> None:
    """List books within a specific genre in the library database."""
    try:
        get_database()
        book_list, column_names = lib.search_book_by_genre(genre)
        print_table(f"Books under genre {genre} are:", book_list, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


@app.command()
def search_by_author(author: str = typer.Option(..., prompt="Author's name")) -> None:
    """List books within a specific author in the library database."""
    try:
        get_database()
        book_list, column_names = lib.search_book_by_author(author)
        print_table(f"Books under author {author} are:", book_list, column_names)
    except sqlite3.Error as e:
        typer.secho(f"Error while checking loan's status: {e}.", fg=typer.colors.RED)
        raise typer.Exit()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit,",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return


def print_table(table_name: str, table_content, column_name):
    column_width = [max(len(str(item[i])) for item in table_content) for i in range(len(column_name))]
    header = " | ".join(f"{column_name[i]:{column_width[i]}}" for i in range(len(column_name)))

    typer.secho(f"\n{table_name}\n", fg=typer.colors.CYAN, bold=True)
    typer.secho(header)
    typer.secho("-" * len(header))
    for row in table_content:
        typer.secho(" | ".join(f"{str(row[i]):{column_width[i]}}" for i in range(len(row))))

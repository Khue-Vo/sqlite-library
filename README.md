# Library

Library is a management app for storing and managing information of books and users in a library.

## Requirements
- The Model-View-Controller pattern
- Command-line interfaces (CLI)
- Python type hints, also known as type annotations
- Object-oriented programming in Python
- SQL, DB Browser for SQLite
- SQL with Python

## Installation

Use github to install and set up the project

```sh
git clone https://github.com/Khue-Vo/sqlite-library.git
```

Navigate to the project directory

```sh
cd ...\sqlite-library
```

## Usage

Use Command-Line Interface (CLI) to operate the project

```sh
Window + R -> cmd -> Enter
```

Access Help Box

```sh
python -m library --help
```

Check version of the app

```sh
python -m library --version
```

Initialize database

```sh
python -m library init
```

Add an author information into the library

```sh
python -m library add-author
```

Add a genre information into the library

```sh
python -m library add-genre
```

Add a book information into the library

```sh
python -m library add-book
```

Add an user information into the library

```sh
python -m library add-user
```

Add a loan information into the library

```sh
python -m library add-loan
```

Update an author information into the library

```sh
python -m library update-author
```

Update a genre information into the library

```sh
python -m library update-genre
```

Update a book information into the library

```sh
python -m library update-book
```

Update an user information into the library

```sh
python -m library update-user
```

Update a loan information into the library

```sh
python -m library update-loan
```

Search for a specific author and check if it's existed within the library

```sh
python -m library search-author
```

Search for a specific genre and check if it's existed within the library

```sh
python -m library search-genre
```

Search for a specific book and check if it's existed within the library

```sh
python -m library search-book
```

Search for a specific user and check if it's existed within the library

```sh
python -m library search-user
```

Search for a specific loan and check if it's existed within the library

```sh
python -m library search-loan
```

Show information of a specific author in the library

```sh
python -m library info-author
```

Show information of a specific genre in the library

```sh
python -m library info-genre
```

Show information of a specific book in the library

```sh
python -m library info-book
```

Show information of a specific user in the library

```sh
python -m library info-user
```

Show information of a specific loan in the library

```sh
python -m library info-loan
```

Show a list of books under the same genre

```sh
python -m library search-by-genre
```

Show a list of books that have the same author

```sh
python -m library search-by-author
```

Show a list of all authors in the database

```sh
python -m library list-all-author
```

Show a list of all genres in the database

```sh
python -m library list-all-genre
```

Show a list of all books in the database

```sh
python -m library list-all-book
```

Show a list of all users in the database

```sh
python -m library list-all-user
```

Show a list of all loans in the database

```sh
python -m library list-all-loan
```

List all books that are available for loan

```sh
python -m library list-available-book
```

List all books that are not available for loan

```sh
python -m library list-non-available-book
```

List all books that are part of a series

```sh
python -m library show-book-in-series
```

List all books that are not part of a series

```sh
python -m library show-book-not-in-series
```

Show author which has the largest number of books in the library

```sh
python -m library show-author-with-most-book
```

Show genre which has the largest number of books in the library

```sh
python -m library show-genre-with-most-book
```

Check if a specific book is available for loan

```sh
python -m library check-available-book
```

Check and show a list of loan that is overdue

```sh
python -m library check-overdue-loan
```

Check and show a list of loan that is returned to the library

```sh
python -m library check-return-loan
```

Check and show a list of user that is currently borrowing books from the library

```sh
python -m library check-user-with-loan
```

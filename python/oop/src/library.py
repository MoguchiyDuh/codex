def _normalize_text(value: str, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")

    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} must not be empty")
    return normalized


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = _normalize_text(title, "title")
        self.author = _normalize_text(author, "author")
        self.pages = pages
        self.is_checked_out = False

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("pages must be an integer")
        if value <= 0:
            raise ValueError(f"pages must be > 0, got {value}")
        self._pages = value

    def checkout(self) -> None:
        if self.is_checked_out:
            raise RuntimeError(f'"{self.title}" is already checked out')
        self.is_checked_out = True

    def return_back(self) -> None:
        if not self.is_checked_out:
            raise RuntimeError(f'"{self.title}" is not checked out')
        self.is_checked_out = False

    def _get_status(self) -> str:
        return "checked out" if self.is_checked_out else "available"

    def __str__(self) -> str:
        return f'Book("{self.title}" by {self.author}, {self._pages}p, {self._get_status()})'

    def __repr__(self) -> str:
        return (
            f"Book(title={self.title!r}, author={self.author!r}, pages={self._pages!r})"
        )


class EBook(Book):
    VALID_FORMATS = {"pdf", "epub", "mobi"}

    def __init__(
        self,
        title: str,
        author: str,
        pages: int,
        file_size_mb: float,
        format: str,
    ) -> None:
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb
        self.format = format

    @property
    def file_size_mb(self) -> float:
        return self._file_size_mb

    @file_size_mb.setter
    def file_size_mb(self, value: float) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("file_size_mb must be a number")
        if value <= 0:
            raise ValueError("file_size_mb must be > 0")
        self._file_size_mb = float(value)

    @property
    def format(self) -> str:
        return self._format

    @format.setter
    def format(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("format must be a string")
        value = value.lower()
        if value not in self.VALID_FORMATS:
            raise ValueError(f"format must be one of {sorted(self.VALID_FORMATS)}")
        self._format = value

    def __str__(self) -> str:
        return (
            f'EBook("{self.title}" by {self.author}, {self._pages}p, '
            f"{self._file_size_mb}MB, .{self._format}, {self._get_status()})"
        )

    def __repr__(self) -> str:
        return (
            f"EBook(title={self.title!r}, author={self.author!r}, "
            f"pages={self._pages!r}, file_size_mb={self._file_size_mb!r}, "
            f"format={self._format!r})"
        )


class Library:
    def __init__(self, name: str) -> None:
        self.name = _normalize_text(name, "name")
        self._books: list[Book] = []

    # ── mutation ──────────────────────────────────────────────────────────────

    def add_book(self, book: Book) -> None:
        if book in self:
            raise ValueError(
                f'A book titled "{book.title}" by {book.author} is already in the library'
            )
        self._books.append(book)

    def remove_book(self, title: str) -> Book:
        book = self._get_or_raise(title)
        self._books.remove(book)
        return book

    def checkout(self, title: str) -> None:
        self._get_or_raise(title).checkout()

    def return_book(self, title: str) -> None:
        self._get_or_raise(title).return_back()

    # ── query ─────────────────────────────────────────────────────────────────

    def find_by_author(self, author: str) -> list[Book]:
        author = _normalize_text(author, "author")
        return [b for b in self._books if b.author.lower() == author.lower()]

    # ── internals ─────────────────────────────────────────────────────────────

    def _get_or_raise(self, title: str) -> Book:
        title = _normalize_text(title, "title")
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        raise KeyError(f'No book titled "{title}" in {self.name}')

    # ── dunders ───────────────────────────────────────────────────────────────

    def __len__(self) -> int:
        return len(self._books)

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return any(book.title.lower() == item.lower() for book in self._books)

        if not isinstance(item, Book):
            return False
        return any(
            (
                b.title.lower() == item.title.lower()
                and b.author.lower() == item.author.lower()
            )
            for b in self._books
        )

    @property
    def borrowed_books_count(self) -> int:
        return sum(book.is_checked_out for book in self._books)

    def __iter__(self) -> list[Book]:
        return iter(self._books)

    def __getitem__(self, index: int) -> Book:
        return self._books[index]

    def __repr__(self) -> str:
        return f"Library(name={self.name!r}, books={len(self)})"


if __name__ == "__main__":
    lib = Library("Alexandria")

    dune = Book("Dune", "Frank Herbert", 412)
    hyperion = Book("Hyperion", "Dan Simmons", 482)
    foundation = Book("Foundation", "Isaac Asimov", 255)
    neuromancer_e = EBook(
        "Neuromancer", "William Gibson", 271, file_size_mb=2.4, format="epub"
    )

    for book in (dune, hyperion, foundation, neuromancer_e):
        lib.add_book(book)

    print(f"Library: {lib!r}")
    print(f"Books in library: {len(lib)}")
    print(f"Borrowed books: {lib.borrowed_books_count}")
    print()

    # __contains__
    print(f'"Dune" in library: {"Dune" in lib}')
    print(f'"Mistborn" in library: {"Mistborn" in lib}')
    print()

    # __iter__
    print("All books:")
    for book in lib:
        print(" ", book)
    print()

    # __getitem__
    print(f"library[0] -> {lib[0]}")
    print()

    # checkout / return
    lib.checkout("Dune")
    print(f"After checkout: {dune}")
    print(f"Borrowed books: {lib.borrowed_books_count}")
    lib.return_book("Dune")
    print(f"After return:   {dune}")
    print(f"Borrowed books: {lib.borrowed_books_count}")
    print()

    # find_by_author
    asimov_books = lib.find_by_author("Isaac Asimov")
    print(f"Books by Isaac Asimov: {asimov_books}")
    print()

    # remove
    removed = lib.remove_book("Hyperion")
    print(f"Removed: {removed}")
    print(f"Library after removal: {len(lib)} books")
    print()

    # validation errors
    print("--- Validation ---")
    try:
        Book("Bad Book", "Author", pages=-5)
    except ValueError as e:
        print(f"pages validation: {e}")

    try:
        EBook("Bad EBook", "Author", 100, file_size_mb=1.0, format="docx")
    except ValueError as e:
        print(f"format validation: {e}")

    try:
        lib.checkout("Dune")
        lib.checkout("Dune")
    except RuntimeError as e:
        print(f"double checkout: {e}")
        lib.return_book("Dune")

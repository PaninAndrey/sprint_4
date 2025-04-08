import pytest
from main import BooksCollector
from data import *


class TestBooksCollector:

    def test_books_genre_is_empty_true(self, book):
        assert len(book.books_genre) == 0

    def test_favorites_is_empty_true(self, book):
        assert len(book.favorites) == 0

    def test_genre_is_actual_true(self, book):
        book_genre = book.genre
        assert book_genre == genre

    def test_genre_age_rating_is_actual_true(self, book):
        book_for_kids = book.genre_age_rating
        assert  book_for_kids == genre_age_rating

    def test_add_new_book_added_one_book_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        new_book = book.books_genre.get(BOOK_TITLE_1)
        assert  new_book == ''

    @pytest.mark.parametrize('name, book_count',
        [
            ([], 0),
            ([BOOK_TITLE_1], 1),
            ([BOOK_TITLE_1, BOOK_TITLE_2], 2),
        ]
    )
    def test_add_new_book_length_true(self, book, name, book_count):
        for book_name in name:
           book.add_new_book(book_name)
        books = book.books_genre
        assert len(books) == book_count

    def test_add_book_genre_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.books_genre[BOOK_TITLE_1] = GENRE
        new_book_genre = book.books_genre[BOOK_TITLE_1]
        assert  new_book_genre == GENRE

    def test_get_book_genre_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.books_genre[BOOK_TITLE_1] = GENRE
        show_book_genre = book.books_genre.get(BOOK_TITLE_1)
        assert  show_book_genre == GENRE

    def test_get_books_with_specific_genre_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.books_genre[BOOK_TITLE_1] = GENRE
        books_with_specific_genre = book.get_books_with_specific_genre(GENRE)
        assert books_with_specific_genre == [BOOK_TITLE_1]

    def test_get_books_genre_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.books_genre[BOOK_TITLE_1] = GENRE
        show_books_genre = book.get_books_genre()
        assert  show_books_genre == {BOOK_TITLE_1 : GENRE}

    def test_get_books_for_children_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.books_genre[BOOK_TITLE_1] = GENRE
        books_for_children = book.get_books_for_children()
        assert  books_for_children == [BOOK_TITLE_1]

    def test_add_book_in_favorites_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.add_book_in_favorites(BOOK_TITLE_1)
        favorites = book.get_list_of_favorites_books()
        assert BOOK_TITLE_1 in favorites

    def test_delete_book_from_favorites_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.add_book_in_favorites(BOOK_TITLE_1)
        book.delete_book_from_favorites(BOOK_TITLE_1)
        favorites = book.get_list_of_favorites_books()
        assert len(favorites) == 0

    @pytest.mark.parametrize('name, book_count',
                             [
                                 ([], 0),
                                 ([BOOK_TITLE_1], 1),
                                 ([BOOK_TITLE_1, BOOK_TITLE_2], 2),
                             ]
                             )
    def test_get_list_of_favorites_books_length(self, book, name, book_count):
        for book_name in name:
            book.add_new_book(book_name)
            book.add_book_in_favorites(book_name)
        favorites = book.get_list_of_favorites_books()
        assert len(favorites) == book_count

    def test_get_list_of_favorites_books_true(self, book):
        book.add_new_book(BOOK_TITLE_1)
        book.add_book_in_favorites(BOOK_TITLE_1)
        favorites = book.get_list_of_favorites_books()
        assert favorites == [BOOK_TITLE_1]
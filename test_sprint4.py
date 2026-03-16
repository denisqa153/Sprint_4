import pytest
from main import BooksCollector
@pytest.fixture
def books_collector():
    return BooksCollector()

class TestBooksCollector: 
    def test_add_new_book_success_created(self, books_collector): #проверка добавления книги в словарь books_genre
        
        name = 'Нига'
        books_collector.add_new_book(name)
        assert name in books_collector.books_genre 
        assert books_collector.books_genre[name] == ''
    

    def test_set_book_genre_establish_genre(self, books_collector): #проверка установления жанра книге

        name = 'Нига'
        genre = 'Фантастика'


        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        assert books_collector.books_genre[name] == genre 

    def test_get_book_genre_output_genre(self, books_collector): # проверка получения жанра книги по имени

        name = 'Нига'
        genre = 'Фантастика'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        result = books_collector.get_book_genre(name)
        assert result == genre


    def test_get_books_genre_output_books_genre(self, books_collector): # проверка получения словаря books_genre
        
        name = 'Нига'
        genre = 'Фантастика'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        result = books_collector.get_books_genre()
        assert result == books_collector.books_genre
    

    def test_add_book_in_favorites_added_favorites(self, books_collector): #проверка добавления книги в избранное
        
        name = 'Нига'
        genre = 'Фантастика'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        books_collector.add_book_in_favorites(name)
        assert name in books_collector.favorites
    

    def test_delete_book_from_favorites_deleted_favorites(self, books_collector): #проверка удаления книги из избранного
        
        name = 'Нига'
        genre = 'Фантастика'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)

        books_collector.delete_book_from_favorites(name)

        assert name not in books_collector.favorites
    

    def test_get_list_of_favorites_books_output_favorites(self, books_collector):     #проверка вывода избранного списка

        
        name = 'Нига'
        genre = 'Фантастика'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)

        result = books_collector.get_list_of_favorites_books()
        
        assert result == [name]



    def test_get_books_for_children_book_fits_baby(self, books_collector): #проверка возврата книг, которые подходят детям
        

        name = 'Нига'
        genre = 'Фантастика'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        result = books_collector.get_books_for_children()
        assert result == [name]

    
    def test_get_books_for_children_book_not_fits_baby(self, books_collector): #проверка возврата книг, которые не подходят детям

        name = 'Нига'
        genre = 'Ужасы'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        result = books_collector.get_books_for_children()
        assert name not in result

    
    @pytest.mark.parametrize(
    "genre",
    ["Фантастика", "Комедии", "Мультфильмы"]
)
    def test_get_books_with_specific_genre_output_specific_genre(self,genre,books_collector): #проверка вывода книги с определенным жанром

        name = 'Нига'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
    
        result = books_collector.get_books_with_specific_genre(genre)
        assert result == [name]
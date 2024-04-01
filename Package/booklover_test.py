import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        book_lover = BookLover("Alice", "alice@example.com", "Fantasy")
        book_lover.add_book("Harry Potter", 5)
        self.assertTrue(book_lover.has_read("Harry Potter"))
    def test_2_add_book(self):
        book_lover = BookLover("Alice1", "alice1@example.com", "Fantasy1")
        book_lover.add_book("Harry Potter1", 4)
        book_lover.add_book("Harry Potter1", 3)
        self.assertEqual(book_lover.num_books_read(), 1) 
        self.assertTrue(book_lover.has_read("Harry Potter1"))
    def test_3_has_read(self): 
        book_lover = BookLover("Alice2", "alic2e@example.com", "Fantasy2")
        book_lover.add_book("Harry Potter2", 5)
        self.assertTrue(book_lover.has_read("Harry Potter2"))
    def test_4_has_read(self): 
        book_lover = BookLover("Alice3", "alice3@example.com", "Fantasy3")
        book_lover.add_book("Dune", 4)
        self.assertFalse(book_lover.has_read("Harry Potter3"))
    def test_5_num_books_read(self): 
        book_lover = BookLover("Alice4", "alice4@example.com", "Fantasy4")
        book_lover.add_book("Harry Potter4", 5)
        book_lover.add_book("Dune1", 4)
        self.assertEqual(book_lover.num_books_read(), 2)
    def test_6_fav_books(self):
        book_lover = BookLover("Alice5", "Alice5@example.com", "Fantasy5")
        book_lover.add_book("Game of Thrones", 5)
        book_lover.add_book("Harry Potter5", 3)
        book_lover.add_book("Lord of the Rings", 4)
        fav_books_df = book_lover.fav_books()
        self.assertTrue(all(fav_books_df['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
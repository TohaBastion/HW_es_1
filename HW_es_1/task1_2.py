"""task1,2"""


class Book:
    """Клас книги"""
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []


    def add_review(self, review_text, reviewer):
        """Додавання відгуку у список відгуків"""
        review = Bookreview(review_text, reviewer)
        self.reviews.append(review)


    def __str__(self):
        book_info = f"'{self.title}', {self.author}, жанр: {self.genre} ({self.year})"
        if self.reviews:
            book_info += "\nВідгуки:"
            for review in self.reviews:
                book_info += f"\n- '{review.review_text}' ({review.reviewer})"
        return book_info


    def __repr__(self):
        return (f"Book(author='{self.author}', title='{self.title}', "
                f"year={self.year}, ganre='{self.genre}')")


class Bookreview:
    """Клас відгук до книги"""
    def __init__(self, review_text, reviewer):
        self.review_text = review_text
        self.reviewer = reviewer


book1 = Book("Джордж Орвелл", "1984", 1948, "Антиутопія")
book2 = Book("Дуглас Адамс", "Путівник по Галактиці для космотуристів", 1979, "Фантастика")
book3 = Book("Ґабрієль Ґарсія Маркес", "Сто років самотності", 1967, "Роман")


book3.add_review('Сама складнонаписана книга яку я читав.', 'Джон Іванович')
book1.add_review('Класика антиутопії!', 'Петро Петров')
book1.add_review('Книга, що все білььше стає реальністю.', 'Невідомий')


print(book1)
print()
print(repr(book1))

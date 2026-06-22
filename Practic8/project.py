from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, Session

engine = create_engine("sqlite:///library.db", echo=True)
print(engine)

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(Integer)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")


Base.metadata.create_all(engine)

with Session(engine) as session:
    author1 = Author(name="Лев Толстой", birth_year=1828)
    author2 = Author(name="Фёдор Достоевский", birth_year=1821)
    author3 = Author(name="Антон Чехов", birth_year=1860)

    session.add_all([author1, author2, author3])
    session.commit()

    book1 = Book(title="Война и мир", year=1869, author_id=author1.id)
    book2 = Book(title="Анна Каренина", year=1877, author_id=author1.id)
    book3 = Book(title="Преступление и наказание", year=1866, author_id=author2.id)
    book4 = Book(title="Идиот", year=1869, author_id=author2.id)
    book5 = Book(title="Чайка", year=1896, author_id=author3.id)

    session.add_all([book1, book2, book3, book4, book5])
    session.commit()

    print(" Все авторы")
    authors = session.query(Author).all()
    for a in authors:
        print(f"{a.name} ({a.birth_year})")

    print(" Изменение имени автора")
    author_to_update = session.query(Author).filter_by(name="Антон Чехов").first()
    author_to_update.name = "А. П. Чехов"
    session.commit()
    print(f"Обновлено: {author_to_update.name}")

    print(" Удаление книги")
    book_to_delete = session.query(Book).filter_by(title="Чайка").first()
    session.delete(book_to_delete)
    session.commit()
    print(f"Удалена книга: {book_to_delete.title}")

    print("Все книги (от новых к старым)")
    books_sorted = session.query(Book).order_by(Book.year.desc()).all()
    for b in books_sorted:
        print(f"{b.title} ({b.year}) - {b.author.name}")

    print("Книги после 1950 года")
    books_after_1950 = session.query(Book).filter(Book.year > 1950).all()
    for b in books_after_1950:
        print(f"{b.title} ({b.year})")
    if not books_after_1950:
        print("Нет книг после 1950 года")

    print("Автор по имени 'Фёдор Достоевский'")
    author = session.query(Author).filter_by(name="Фёдор Достоевский").first()
    print(f"{author.name}, род. {author.birth_year}")

    print("Количество книг")
    count = session.query(func.count(Book.id)).scalar()
    print(f"Всего книг: {count}")

    print(" Первые 3 книги по алфавиту")
    books_alpha = session.query(Book).order_by(Book.title).limit(3).all()
    for b in books_alpha:
        print(f"{b.title} ({b.year})")

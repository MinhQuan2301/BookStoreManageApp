from app.models import Category, Book, User, Author, Publish
from app import app
import hashlib
from sqlalchemy import func, or_


def get_category():
    return Category.query.all()


def count_book():
    return Book.query.count()


# def check_login(username, password):
#     password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#     return User.query.filter(User.username.__eq__(username.strip()),
#                              User.password.__eq__(password)).first()


def get_book(kw, cate_id, page=None):
    book = Book.query
    if kw:
        book = book.join(Author)
    book = book.join(Publish)

    if kw:

        book = book.filter(or_(func.lower(Book.BookName).contains(func.lower(kw)),
                               func.lower(Author.AuthorName).contains(func.lower(kw)),
                               func.lower(Publish.Publish_Name).contains(func.lower(kw))))

    if cate_id:
        book = book.filter(Book.Category_ID.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1)*page_size

        return book.slice(start, start + page_size)

    return book.all()

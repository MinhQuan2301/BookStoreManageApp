from Project.models import Category, Book, User, Author
from Project import app
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


def get_book(kw, cate_id, page = None):
    book = Book.query
    if kw:
        book = book.join(Author)

    if kw:

        book = book.filter(or_(func.lower(Book.name).contains(func.lower(kw)),
                               func.lower(Author.FullName).contains(func.lower(kw))))

    if cate_id:
        book = book.filter(Book.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config["PAGE_SIZE"]
        start = (page - 1)*page_size

        return book.slice(start, start + page_size)


    return book.all()

from Project.models import Category, Book, User
from Project import app
import hashlib


def get_category():
    return Category.query.all()

def check_login(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


def get_book(kw, cate_id):
    book = Book.query
    if kw:
        book = book.filter(Book.name.contains(kw))

    if cate_id:
        book = book.filter(Book.category_id.__eq__(cate_id))

    return book.all()
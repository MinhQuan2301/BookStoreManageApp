from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, CheckConstraint,Enum, Text
from sqlalchemy.orm import relationship
from Project import db,app
from flask_login import UserMixin
import hashlib, enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    def __str__(self):
        return self.name
class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Book', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Book(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255), default=True)
    active = Column(Boolean, default=True)
    info = Column(String(255), default=True, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    __table_args__ = (
        CheckConstraint('quantity >= 0', name='quantity_non_negative'),
        CheckConstraint('quantity >= 5 AND quantity < 50', name='quantity_range'),
    )

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # c1 = Category(name="Tiểu thuyết")
        # c2 = Category(name="Trinh thám ")
        # c3 = Category(name="Kinh doanh và tài chính")
        # c4 = Category(name="Tâm lý học")
        # c5 = Category(name="Khoa học và Thiên văn học ")
        # c6 = Category(name="Lịch sử và Văn hóa")
        # c7 = Category(name="Nấu ăn và ẩm thực ")
        # c8 = Category(name="Trẻ em và thiếu nhi")
        # db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])
        # db.session.commit()
        # s1 = Book(name="Mười người da đen nhỏ", price=135000, category_id=1,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s2 = Book(name="Phía Sau Nghi Can X ", price=150000, category_id=2,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s3 = Book(name="Bí quyết gây dựng cơ nghiệp bạc tỷ", price=135000, category_id=3,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s4 = Book(name="Tấm lý học đám đông", price=135000, category_id=4,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s5 = Book(name="Từ điển thiên văn học và vật lý thiên văn", price=135000, category_id=5,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s6 = Book(name="Lịch sử và văn hóa Đông Nam Á", price=135000, category_id=6,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s7 = Book(name="Ăn uống thời hiện đại", price=135000, category_id=7,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s8 = Book(name="Kể truyện cho bé tuổi mầm non", price=135000, category_id=8,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s9 = Book(name="Tiểu thuyết hay 2021", price=135000, category_id=1,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s10 = Book(name="Mật mã Da Vinci", price=135000, category_id=2,
        #           image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           quantity=5, info="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10])
        # db.session.commit()
        # u1 = User(name=' Admin ', username="admin",
        #             password=str(hashlib.md5('12345'.encode('utf-8')).hexdigest()),
        #             user_role = UserRoleEnum.ADMIN)
        # db.session.add_all([u1])
        # db.session.commit()

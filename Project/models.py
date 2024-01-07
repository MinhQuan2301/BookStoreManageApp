from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, CheckConstraint,Enum, TEXT, CHAR, Date, DateTime
from sqlalchemy.orm import relationship
from Project import db, app
from flask_login import UserMixin
import hashlib, enum
from datetime import datetime



class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class Staff(db.Model):
    Staff_ID = Column(Integer, primary_key=True, autoincrement=True)
    FullName = Column(String(255), nullable=False, unique=True)
    Gender = Column(String(10), nullable=True)
    Starting_Date = Column(DateTime, default=datetime.now())
    Position = Column(String(255), nullable=False)

    user = relationship('User', back_populates='staff')


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    Account_ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False, unique=True)
    Username = Column(String(50), nullable=False, unique=True)
    Password = Column(String(50), nullable=False)
    Staff_ID = Column(Integer, ForeignKey(Staff.Staff_ID), nullable=False)
    User_Role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    staff = relationship('Staff', back_populates='user')


class Customer(db.Model):
    __tablename__ = 'Customer'
    Customer_ID = Column(CHAR(10), primary_key=True, nullable=True, unique=True)
    FullName = Column(String(255), nullable=True)
    Gender = Column(String(10), nullable=True)
    BirthDay = Column(Date)

    phone_number = relationship('PhoneNumber', back_populates='customer')
    delivery_of_customer = relationship('DeliveryOfCustomer', back_populates='customer')


class PhoneNumber(db.Model):
    Phone_Number_ID = Column(Integer, primary_key=True, autoincrement=True)
    PhonE_Number = Column(CHAR(10), nullable=True, unique=True)
    Customer_ID = Column(CHAR(10), ForeignKey(Customer.Customer_ID), nullable=False)

    customer = relationship('Customer', back_populates='phone_number')


class DeliveryAddress(db.Model):
    Address_ID = Column(Integer, primary_key=True, autoincrement=True)
    Address = Column(String(255), nullable=True)

    delivery_of_customer = relationship('DeliveryOfCustomer', back_populates='address')


class DeliveryOfCustomer(db.Model):
    DOC_ID = Column(Integer, primary_key=True, autoincrement=True)
    Address_ID = Column(Integer, ForeignKey(DeliveryAddress.Address_ID), nullable=False)
    Customer_ID = Column(CHAR(10), ForeignKey(Customer.Customer_ID), nullable=False)

    address = relationship('DeliveryAddress', back_populates='delivery_of_customer')
    customer = relationship('Customer', back_populates='delivery_of_customer')


class Category(db.Model):
    __tablename__ = 'Category'
    Category_ID = Column(Integer, primary_key=True, autoincrement=True)
    Category_Name = Column(String(50), nullable=False, unique=True)

    books = relationship('Book', back_populates='category', lazy=True)


class Author(db.Model):
    __tablename__ ='Author'
    Author_ID = Column(Integer, primary_key=True, autoincrement=True)
    AuthorName = Column(String(255), nullable=False, unique=True)
    Gender = Column(String(25), nullable=False, default='unknow')
    Year_Of_Birth = Column(Integer, nullable=False, default=0)

    books = relationship('Book', back_populates='author')


class Publish(db.Model):
    __tablename__ = 'Publish'
    Publish_ID = Column(Integer, primary_key=True, autoincrement=True)
    Publish_Name = Column(String(255), nullable=False, unique=True)
    Publish_Address = Column(String(255), nullable=False, unique=True)

    books = relationship('Book', back_populates='publish')


class Book(db.Model):
    __tablename__ = 'Book'
    Book_ID = Column(Integer, primary_key=True, autoincrement=True)
    BookName = Column(String(50), nullable=False, unique=True)
    Price = Column(Float, default=0)
    Image = Column(String(255), default=True)
    Active = Column(Boolean, default=True)
    BookInfo = Column(String(1000), default=True, nullable=False)
    QuantityInTook = Column(Integer, nullable=False, default=0)
    Category_ID = Column(Integer, ForeignKey(Category.Category_ID), nullable=False)
    Author_ID = Column(Integer, ForeignKey(Author.Author_ID), nullable=False)
    Publish_ID = Column(Integer, ForeignKey(Publish.Publish_ID), nullable=False)
    category = relationship('Category', back_populates='books')
    author = relationship('Author', back_populates='books')
    bill_detail = relationship('BillDetail', back_populates='books')
    publish = relationship('Publish', back_populates='books')


class Bill(db.Model):
    __tablename__ = 'Bill'
    Bill_ID = Column(Integer, primary_key=True, autoincrement=True)
    Total_Amount = Column(Integer, nullable=True)
    Book_Receive_At = Column(Integer)
    State = Column(Boolean)
    Customer_ID = Column(CHAR(10), ForeignKey(Customer.Customer_ID), nullable=False)

    bill_detail = relationship('BillDetail', back_populates='bill')


class BillDetail(db.Model):
    __tablename_ = 'BillDetail'
    Bill_Detail_ID = Column(Integer, primary_key=True, autoincrement=True)
    Quantity = Column(Integer, nullable=False, default=0)
    Order_Date = Column(DateTime, default=datetime.now())
    Bill_ID = Column(Integer, ForeignKey(Bill.Bill_ID), nullable=False)
    Book_ID = Column(Integer, ForeignKey(Book.Book_ID), nullable=False)

    bill = relationship('Bill', back_populates='bill_detail')
    books = relationship('Book', back_populates='bill_detail')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # c1 = Category(Category_Name="Tiểu thuyết")
        # c2 = Category(Category_Name="Trinh thám ")
        # c3 = Category(Category_Name="Kinh doanh và tài chính")
        # c4 = Category(Category_Name="Tâm lý học")
        # c5 = Category(Category_Name="Khoa học và Thiên văn học ")
        # c6 = Category(Category_Name="Lịch sử và Văn hóa")
        # c7 = Category(Category_Name="Nấu ăn và ẩm thực ")
        # c8 = Category(Category_Name="Trẻ em và thiếu nhi")
        # db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])
        # db.session.commit()
        #
        # p1 = Publish(Publish_Name="Nhà xuất bản Trẻ", Publish_Address="161B Lý Chính Thắng; Phường 7; Quận 3; Thành phố Hồ Chí Minh.")
        # p2 = Publish(Publish_Name="Nhà xuất bản Kim Đồng", Publish_Address="248 Đ. Cống Quỳnh, Phường Phạm Ngũ Lão, Quận 1, Thành phố Hồ Chí Minh")
        # p3 = Publish(Publish_Name="Nhà xuất bản Tổng hợp thành phố Hồ Chí Minh", Publish_Address="62 Nguyễn Thị Minh Khai, phường Đa Kao, quận 1, TPHCM")
        # p4 = Publish(Publish_Name="Nhà xuất bản Lao Động", Publish_Address="82 Trần Hưng Đạo, Hà Nộ")
        # p5 = Publish(Publish_Name="Nhà xuất bản Hội Nhà văn", Publish_Address="65, Nguyễn Du, quận Hai Bà Trưng, Hà Nội")
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
        #
        # a1 = Author(AuthorName='Nguyễn Ái Quốc', Gender='Nam', Year_Of_Birth=1890)
        # a2 = Author(AuthorName='Hồ Xuân Hương', Gender='Nữ', Year_Of_Birth=1772)
        # a3 = Author(AuthorName='Nguyễn Du', Gender='Nam', Year_Of_Birth=1766)
        # a4 = Author(AuthorName='Nguyễn Nhật Ánh', Gender='Nam', Year_Of_Birth=1955)
        # a5 = Author(AuthorName='Nguyễn Ngọc Thạch', Gender='Nam', Year_Of_Birth=1987)
        # db.session.add_all([a1, a2, a3, a4, a5])
        # db.session.commit()
        #
        # s1 = Book(BookName="Mười người da đen nhỏ", Price=135000, Category_ID=1, Author_ID='1', Publish_ID=1,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s2 = Book(BookName="Phía Sau Nghi Can X ", Price=150000, Category_ID=2, Author_ID='2', Publish_ID=2,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s3 = Book(BookName="Bí quyết gây dựng cơ nghiệp bạc tỷ", Price=135000, Category_ID=3, Author_ID='3', Publish_ID=3,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s4 = Book(BookName="Tấm lý học đám đông", Price=135000, Category_ID=4, Author_ID='4', Publish_ID=4,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s5 = Book(BookName="Từ điển thiên văn học và vật lý thiên văn", Price=135000, Category_ID=5, Author_ID='5', Publish_ID=5,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s6 = Book(BookName="Lịch sử và văn hóa Đông Nam Á", Price=135000, Category_ID=6, Author_ID='1', Publish_ID=1,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s7 = Book(BookName="Ăn uống thời hiện đại", Price=135000, Category_ID=7, Author_ID='2', Publish_ID=2,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s8 = Book(BookName="Kể truyện cho bé tuổi mầm non", Price=135000, Category_ID=8, Author_ID='3', Publish_ID=3,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s9 = Book(BookName="Tiểu thuyết hay 2021", Price=135000, Category_ID=1, Author_ID='4', Publish_ID=4,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # s10 = Book(BookName="Mật mã Da Vinci", Price=135000, Category_ID=2, Author_ID='5', Publish_ID=5,
        #           Image="https://i.pinimg.com/originals/91/76/9a/91769a5f3c3d663cc3c2152e9fadabf0.jpg",
        #           QuantityInTook=5, BookInfo="Tiểu thuyết nói về vụ án bí ẩn trên hòn đảo Soldier Island với 10 người bằng cách này hay cách khác đã thiệt mạng mà không hề có sự hiện diện hay dấu vết của thủ phạm")
        # db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10])
        # db.session.commit()
        #
        # t1 = Staff(FullName="Nguyễn Đình Nhật", Gender="Nam", Position="Thời vụ")
        # db.session.add(t1)
        # db.session.commit()
        #
        # u1 = User(Name=' Admin ', Username="admin",
        #           Password=str(hashlib.md5('12345'.encode('utf-8')).hexdigest()),
        #           User_Role = UserRoleEnum.ADMIN, Staff_ID=1)
        # db.session.add_all([u1])
        # db.session.commit()

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from flask_login import UserMixin

# Определяем базовый класс
Base = declarative_base()


# Определяем модель для таблицы авторов
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    quotes = relationship('Quote', back_populates='author')


# Определяем модель для таблицы тем
class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    quotes = relationship('Quote', back_populates='topic')


# Определяем модель для таблицы цитат
class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    # date = Column(DateTime(timezone=True), default=func.now())
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)

    def __init__(self, text, author_id, topic_id):
        self.topic_id = topic_id
        self.text = text
        self.author_id = author_id

    author = relationship('Author', back_populates='quotes')
    topic = relationship('Topic', back_populates='quotes')
    user_quote = relationship('UserQuote', back_populates='quote')


class UserQuote(Base):
    __tablename__ = 'userquotes'
    id = Column(Integer, primary_key=True)
    quote_id = Column(Integer, ForeignKey('quotes.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, quote_id, user_id):
        self.quote_id = quote_id
        self.user_id = user_id

    user = relationship('User', back_populates='user_quotes')
    quote = relationship('Quote', back_populates='user_quote')


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True)
    password = Column(String(150))
    first_name = Column(String(150))
    last_name = Column(String(150))
    login = Column(String(150))
    # date = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, email, password, first_name, last_name, login):
        self.login = login
        self.last_name = last_name
        self.first_name = first_name
        self.password = password
        self.email = email

    user_quotes = relationship('UserQuote', back_populates='user')

    def is_active(self):
        return True

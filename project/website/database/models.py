from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Определяем базовый класс
Base = declarative_base()

# Определяем модель для таблицы авторов
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    quotes = relationship('Quote', back_populates='author')

# Определяем модель для таблицы тем
class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    quotes = relationship('Quote', back_populates='topic')

# Определяем модель для таблицы цитат
class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    #date = Column(DateTime(timezone=True), default=func.now())
    authorId = Column(Integer, ForeignKey('authors.id'), nullable=False)
    topicId = Column(Integer, ForeignKey('topics.id'), nullable=False)

    author = relationship('Author', back_populates='quotes')
    topic = relationship('Topic', back_populates='quotes')
    userQuote = relationship('UserQuote', back_populates='quote')

class UserQuote(Base):
    __tablename__ = 'userquotes'
    id = Column(Integer, primary_key=True)
    quoteId = Column(Integer, ForeignKey('quotes.id'), nullable=False)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship('User', back_populates='userQuotes')
    quote = relationship('Quote', back_populates='userQuote') 

from flask_login import UserMixin
class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True)
    password = Column(String(150))
    firstName = Column(String(150))
    lastName = Column(String(150))
    login = Column(String(150))
    #date = Column(DateTime(timezone=True), default=func.now())

    userQuotes = relationship('UserQuote', back_populates='user')

    def is_active(self):
        return self.active


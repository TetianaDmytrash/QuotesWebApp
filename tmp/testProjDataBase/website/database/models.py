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
    authorId = Column(Integer, ForeignKey('authors.id'), nullable=False)
    topicId = Column(Integer, ForeignKey('topics.id'), nullable=False)

    author = relationship('Author', back_populates='quotes')
    topic = relationship('Topic', back_populates='quotes')
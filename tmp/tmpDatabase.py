from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker
from flask import Flask, render_template

app = Flask(__name__)

# Создаем подключение к базе данных (замените 'sqlite:///example.db' на ваш URL)
engine = create_engine('sqlite:///example.db', echo=True)

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

# Очистка базы данных
Base.metadata.drop_all(engine)

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
#Session = sessionmaker(bind=engine)
#session = Session()
session = Session(engine)

# Список кортежей с данными
with open('quotesListTMP.txt') as ffile:
   contents = ffile.readlines()
   data = [tuple(quate.strip().split(' | ')) for quate in contents]

# Заполняем таблицы данными из списка
for topicName, quoteText, authorName in data:
    #print(f"!!!!!!!!!!qoute: {topicName}, {quoteText} | {authorName}")
    author = session.query(Author).filter_by(name=authorName).first()
    #print(f"author: {author}")
    #print(f"find author in list")
    if not author:
        author = Author(name=authorName)
        session.add(author)
        session.commit()
        #print(f"add new author: {author}")
    
    topic = session.query(Topic).filter_by(name=topicName).first()
    #print(f"topic: {topic}")
    #print(f"find topic in list")
    if not topic:
        topic = Topic(name=topicName)
        session.add(topic)
        session.commit()
        #print(f"add new topic: {topic}")

    quote = Quote(text=quoteText, authorId=author.id, topicId=topic.id)
    session.add(quote)
    #print(f'create row in quate: {quote.text}')
    

session.commit()

# Выводим все записи из таблицы topics
print("Topics:")
for topic in session.query(Topic).all():
    print(f"{topic.id}: {topic.name}")

# Выводим все записи из таблицы авторов
print("Authors:")
for author in session.query(Author).all():
    print(f"{author.id}: {author.name}")

# Выводим все записи из таблицы цитат
print("\nQuotes:")
for quote in session.query(Quote).all():
    print(f"Topic: {quote.topic.id}: {quote.topic.name}")
    print(f"{quote.id}: {quote.text} (Author: {quote.author.name})")


# Flask-маршрут для отображения данных
@app.route('/')
def index():
    authors = session.query(Author).all()
    topics = session.query(Topic).all()
    quotes = session.query(Quote).all()
    return render_template('index.html', authors=authors, topics=topics, quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)

session.close()
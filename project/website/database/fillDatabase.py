from .database import session
from .models import Author, Topic, Quote
from project.logger import logger


def fill_database():
    # Список кортежей с данными
    with open('C:\\proj_2023\\PeEx\\QuotesWebApp\\project\\website\\database\\quoteFile.txt') as ffile:
        contents = ffile.readlines()
        data = [tuple(quote.strip().split(' | ')) for quote in contents]

    # Заполняем таблицы данными из списка
    for topic_name, quote_text, author_name in data:
        logger.warning(f"quote: {topic_name}, {quote_text} | {author_name}")
        author = session.query(Author).filter_by(name=author_name).first()
        logger.warning(f"author: {author}")
        logger.warning(f"find author in list")
        if not author:
            author = Author(name=author_name)
            session.add(author)
            session.commit()
            logger.warning(f"add new author: {author}")

        topic = session.query(Topic).filter_by(name=topic_name).first()
        logger.warning(f"topic: {topic}")
        logger.warning(f"find topic in list")
        if not topic:
            topic = Topic(name=topic_name)
            session.add(topic)
            session.commit()
            logger.warning(f"add new topic: {topic}")

        quote = Quote(text=quote_text, author_id=author.id, topic_id=topic.id)
        session.add(quote)
        logger.warning(f'create row in quote: {quote.text}')

    session.commit()

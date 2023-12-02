from .database import session
from .models import Author, Topic, Quote
from logger import logger

def fillDatabase():
	# Список кортежей с данными
	with open('C:\\proj_2023\\PeEx\\QuotesWebApp\\project\\website\\database\\quoteFile.txt') as ffile:
	   contents = ffile.readlines()
	   data = [tuple(quate.strip().split(' | ')) for quate in contents]

	# Заполняем таблицы данными из списка
	for topicName, quoteText, authorName in data:
	    logger.warning(f"qoute: {topicName}, {quoteText} | {authorName}")
	    author = session.query(Author).filter_by(name=authorName).first()
	    logger.warning(f"author: {author}")
	    logger.warning(f"find author in list")
	    if not author:
	        author = Author(name=authorName)
	        session.add(author)
	        session.commit()
	        logger.warning(f"add new author: {author}")
	    
	    topic = session.query(Topic).filter_by(name=topicName).first()
	    logger.warning(f"topic: {topic}")
	    logger.warning(f"find topic in list")
	    if not topic:
	        topic = Topic(name=topicName)
	        session.add(topic)
	        session.commit()
	        logger.warning(f"add new topic: {topic}")

	    quote = Quote(text=quoteText, authorId=author.id, topicId=topic.id)
	    session.add(quote)
	    logger.warning(f'create row in quate: {quote.text}')
	    

	session.commit()

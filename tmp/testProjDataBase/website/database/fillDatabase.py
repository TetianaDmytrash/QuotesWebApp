from .database import session
from .models import Author, Topic, Quote

def fillDatabase():
	# Список кортежей с данными
	with open('C:\\proj_2023\\PeEx\\QuotesWebApp\\tmp\\testProjDataBase\\website\\database\\quotesListTMP.txt') as ffile:
	   contents = ffile.readlines()
	   data = [tuple(quate.strip().split(' | ')) for quate in contents]

	# Заполняем таблицы данными из списка
	for topicName, quoteText, authorName in data:
	    print(f"qoute: {topicName}, {quoteText} | {authorName}")
	    author = session.query(Author).filter_by(name=authorName).first()
	    print(f"author: {author}")
	    print(f"find author in list")
	    if not author:
	        author = Author(name=authorName)
	        session.add(author)
	        session.commit()
	        print(f"add new author: {author}")
	    
	    topic = session.query(Topic).filter_by(name=topicName).first()
	    print(f"topic: {topic}")
	    print(f"find topic in list")
	    if not topic:
	        topic = Topic(name=topicName)
	        session.add(topic)
	        session.commit()
	        print(f"add new topic: {topic}")

	    quote = Quote(text=quoteText, authorId=author.id, topicId=topic.id)
	    session.add(quote)
	    print(f'create row in quate: {quote.text}')
	    

	session.commit()

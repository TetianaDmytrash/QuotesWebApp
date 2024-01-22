"""
fill database data from file
"""
from .database import session
from .models import Author, Topic, Quote
from logs.logger import logger

import os


def fill_database():
    """
    main function for fill data
    add some comments for feature_branch_test
    """
    # List of tuples with data
    current_folder_path = os.getcwd() + "/app/database/quote_file.txt"
    # open('/home/flask/Documents/QuotesWebApp/app/database/quote_file.txt')
    with open(current_folder_path) as ffile:
        contents = ffile.readlines()
        data = [tuple(quote.strip().split(' | ')) for quote in contents]

    # Fill tables with data from the list
    for topic_name, quote_text, author_name in data:
        logger.warning("quote: {}, {} | {}".format(topic_name, quote_text, author_name))
        author = session.query(Author).filter_by(name=author_name).first()
        logger.warning("author: {}".format(author))
        logger.warning("find author in list")
        if not author:
            author = Author(name=author_name)
            session.add(author)
            session.commit()
            logger.warning("add new author: {}".format(author))

        topic = session.query(Topic).filter_by(name=topic_name).first()
        logger.warning("topic: {}".format(topic))
        logger.warning("find topic in list")
        if not topic:
            topic = Topic(name=topic_name)
            session.add(topic)
            session.commit()
            logger.warning("add new topic: {}".format(topic))

        quote = Quote(text=quote_text, author_id=author.id, topic_id=topic.id)
        session.add(quote)
        logger.warning("create row in quote: {}".format(quote.text))

    session.commit()

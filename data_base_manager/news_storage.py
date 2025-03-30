from dataclasses import asdict
from logging import Logger
from pymongo import MongoClient

from models import ArticleModel
from news_module.news_article import NewsArticle


class NewsStorage:
    def __init__(self, mongo_client: MongoClient, db_name: str, logger: Logger):
        self.mongo_client = mongo_client
        self.db_name = db_name
        self.logger = logger

    def store_articles_staging(self, collection_name: str, article_list: list[NewsArticle]):
        if not article_list:
            self.logger.info("No articles to save!")

        # news_article_insert = [article.__dict__ for article in article_list]
        news_article_insert = [ArticleModel(**asdict(article)).model_dump(by_alias=True) for article in
                               article_list]

        self.mongo_client.insert_data(self.db_name, collection_name, news_article_insert)

    def move_articles_prod(self, staging_collection: str, prod_collection: str):
        db = self.mongo_client.client[self.db_name]
        staging_collection = db[staging_collection]
        prod_collection = db[prod_collection]

        # Find articles in staging that are not in main collection
        pipeline = [
            {"$lookup": {
                "from": "news_collection",
                "localField": "url",
                "foreignField": "url",
                "as": "existing_articles"
            }},
            {"$match": {"existing_articles": {"$size": 0}}},  # Keep only non-duplicate articles
            {"$project": {"existing_articles": 0}}  # Remove the "existing_articles" field from the result
        ]

        # Perform the aggregation to find unique articles
        unique_articles = list(staging_collection.aggregate(pipeline))

        if unique_articles:
            # Insert unique articles into main collection
            prod_collection.insert_many(unique_articles)
            self.logger.info(f"Moved {len(unique_articles)} articles to main.")

            # Delete moved articles from staging collection
            staging_collection.delete_many({})
            self.logger.info("Staging collection cleaned up.")

            # Optionally, if there are no unique articles, you can clean the staging collection completely
        else:
            self.logger.info("No unique articles found to move.")
            # Clean the entire staging collection if desired (or leave it for the next batch)
            staging_collection.delete_many({})
            self.logger.info("Staging collection cleaned up.")


from gdelt import GdeltDoc, Filters
from news_module import NewsPaperProcessor
from enricher_module import EnrichmentOrchestrator
from data_base_manager import MongoManger, NewsStorage
from logging import config
import logging



def main():
    config.fileConfig("logging.conf")
    logger = logging.getLogger("happy_log")

    f = Filters(
        country= "us",
        timespan="24h",
        num_records=50
        )

    message = f"""
        Fetching news from API!
        Filters: str({f})
    """
    logger.info(message)

    gd = GdeltDoc()
    articles = gd.article_search(f)

    nr_articles = len(articles["articles"])
    logger.info(f"Nr of articles: {nr_articles}.")

    news_processor = NewsPaperProcessor(news_collection_raw=articles)
    news_processor.process_articles()
    logger.info("Articles are processed, ready to be enriched!")

    list_news_instances = news_processor.news_collection
    enrichment_orchestrator = EnrichmentOrchestrator(list_news_instances=list_news_instances,
                                                     logger=logger)
    enrichment_orchestrator.process_enrichments()

    print(list_news_instances)
    mongo_client = MongoManger()
    news_storage = NewsStorage(mongo_client=mongo_client,
                               logger=logger,
                               db_name="NEWS_DB")

    news_storage.store_articles_staging(
        collection_name="staging_news_collection",
        article_list=list_news_instances)

    news_storage.move_articles_prod(
        staging_collection="staging_news_collection",
        prod_collection="news_collection")



if __name__ == "__main__":
    main()











from concurrent.futures import ThreadPoolExecutor
from logging import Logger
from typing import List

from news_module.news_article import NewsArticle
from enricher_module.text_fetcher import fetch_full_text
from enricher_module.sentiment_manager import SentimentManager


class EnrichmentOrchestrator:
    def __init__(self, list_news_instances: List[NewsArticle], logger: Logger):
        self.list_news_instances = list_news_instances
        self.sentiment_manager = SentimentManager()
        self.logger = logger

    def _enrich_single_article(self, article):
        try:
            self.logger.info(f"Processing {article.url}")

            full_article_text = fetch_full_text(article.url)
            article.fullText = full_article_text if full_article_text else article.title

            sentiment_details = self.sentiment_manager.fetch_sentiment(article.fullText)
            article.sentimentLabel, article.sentimentScore = sentiment_details
        except Exception as e:
            self.logger.error(f"Error processing article {article.url}: {str(e)}")

    def process_enrichments(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self._enrich_single_article, self.list_news_instances)






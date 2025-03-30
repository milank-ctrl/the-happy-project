from dataclasses import dataclass, field
from typing import Dict, List, Union
from news_module.news_article import NewsArticle



@dataclass
class NewsPaperProcessor:
    news_collection_raw: Dict[str, List[Dict]]
    news_collection: list[NewsArticle] = field(default_factory=list)

    def process_articles(self):
        self.news_collection = [
            NewsArticle(
                url=article.get("url", ""),
                title=article.get("title", "Unknown"),
                seenDate=article.get("seendate", ""),
                domain=article.get("domain", ""),
                language=article.get("language", ""),
                sourceCountry=article.get("sourcecountry", ""),
                socialImage=article.get("socialimage", ""),
            )
            for article in self.news_collection_raw.get("articles", [])
        ]


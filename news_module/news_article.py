from dataclasses import dataclass
from typing import Union


@dataclass
class NewsArticle:
    url: str
    title: str
    seenDate: str
    domain: str
    language: str
    sourceCountry: str
    socialImage: str
    fullText: Union[str, None] = None
    sentimentScore: Union[float, None] = None
    sentimentLabel: Union[str, None] = None
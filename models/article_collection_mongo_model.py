from typing import List
from . import ArticleModel
from pydantic import BaseModel


class ArticleCollection(BaseModel):
    """
    A container holding a list of `NewsArticleModel` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    article_collection: List[ArticleModel]

from newspaper import Article
from newspaper.article import ArticleException

def fetch_full_text(article_url: str):
    try:
        article_web = Article(article_url)
        article_web.download()
        article_web.parse()
        return article_web.text[:150]
    except ArticleException as e:
        print(f"Error during fetching article text: {str(e)}")
        return None

import certifi
from fastapi import FastAPI
from motor import motor_asyncio
import os
from models import ArticleModel, ArticleCollection
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="The Positive News API",
    summary="A sample application showing only positive news",
)

client = motor_asyncio.AsyncIOMotorClient(
    os.getenv("MONGO_URI"),
    tlsCAFile=certifi.where())

db = client.NEWS_DB
news_collection = db.get_collection("news_collection")

@app.get(
    "/articles/",
    response_description="List all articles",
    response_model=ArticleCollection,
    response_model_by_alias=False,
)
async def list_articles(

):
    """
    List all of the article data in the database.

    The response is unpaginated and limited to 1000 results.
    """
    return ArticleCollection(article_collection=await news_collection.find().to_list(1000))
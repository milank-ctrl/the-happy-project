import uuid
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator


class ArticleModel(BaseModel):
    """Container for single news article record."""

    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    url: str = Field(...)
    title: str = Field(...)
    seenDate: datetime = Field(...)
    domain: str = Field(...)
    language: str = Field(...)
    sourceCountry: str = Field(...)
    socialImage: Optional[str]
    fullText: str = Field(...)
    sentimentScore: float = Field(...)
    sentimentLabel: Literal["NEGATIVE", "POSITIVE", "NEUTRAL"]


    @field_validator("seenDate", mode="before")
    @classmethod
    def parse_seen_date(cls, v):
        if isinstance(v, str):  # Convert string to datetime
            return datetime.strptime(v, "%Y%m%dT%H%M%SZ")
        return v  # If it's already a datetime, return as is

    class Config:

        # Example configuration for schema
        json_schema_extra = {
            "example": {
                "url": "https://wupe.com/ixp/295/p/best-album-80s-poll-round-three/",
                "title": "Vote for the Best Album of the 80s : Only the Elite 8 Remain !",
                "seenDate": "20250328T161500Z",
                "domain": "wupe.com",
                "language": "English",
                "sourceCountry": "United States",
                "socialImage": "https://townsquare.media/site/295/files/2025/03/attachment-UCRBracket_v2MWPERSON.jpg?&q=75&format=natural",
                "fullText": "After two big rounds of voting, just eight elite '80s classic rock albums are left to vie for your votes in round three of our March Madness bracket.\n",
                "sentimentScore": "NEGATIVE",
                "sentimentLabel": "POSITIVE"
            }
        }

        # Added configurations
        populate_by_name = True  # Allow population by name
        arbitrary_types_allowed = True  # Allow arbitrary types in the model




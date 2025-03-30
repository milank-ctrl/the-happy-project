from transformers import pipeline, Pipeline


class SentimentManager:
    _sentiment_pipeline: Pipeline = None

    def __init__(self):
        if not SentimentManager._sentiment_pipeline:
            try:
                SentimentManager._sentiment_pipeline \
                    = pipeline(
                        task="sentiment-analysis",
                        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
            except Exception as e:
                print(f"Sentiment pipeline load failed: {str(e)}")

    def fetch_sentiment(self, text: str):
        try:
            result = SentimentManager._sentiment_pipeline(text)
            label = result[0]["label"]
            score = result[0]["score"]
        except:
            label = "NEUTRAL"
            score = 0.0

        return label, score


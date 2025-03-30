export interface NewsArticle {
  id: string
  url: string
  title: string
  seenDate: string
  domain: string
  language: string
  sourceCountry: string
  socialImage?: string
  fullText: string
  sentimentScore: number
  sentimentLabel: "NEGATIVE" | "POSITIVE" | "NEUTRAL"
}

export interface ArticleCollection {
  article_collection: NewsArticle[]
}


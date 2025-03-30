import type { ArticleCollection, NewsArticle } from "./types"

// Update to use the actual API endpoint
export async function fetchNews(): Promise<NewsArticle[]> {
  try {
    const response = await fetch("http://localhost:8000/articles/")
    if (!response.ok) {
      console.error("Failed to fetch articles:", response.statusText)
      return []
    }

    const data: ArticleCollection = await response.json()
    return data.article_collection
  } catch (error) {
    console.error("Error fetching news:", error)
    return []
  }
}

export async function fetchNewsById(id: string): Promise<NewsArticle | null> {
  try {
    // First fetch all articles since there's no endpoint for a single article
    const articles = await fetchNews()

    // Find the article with the matching ID
    return articles.find((article) => article.id === id) || null
  } catch (error) {
    console.error("Error fetching article by ID:", error)
    return null
  }
}

// Keep the mock data for development/testing
const mockNews: NewsArticle[] = [
  {
    id: "1",
    url: "https://example.com/news/1",
    title: "Global Tech Giants Announce Collaboration on AI Ethics",
    seenDate: "2023-05-15T10:30:00Z",
    domain: "example.com",
    language: "en",
    sourceCountry: "US",
    socialImage: "/placeholder.svg?height=400&width=600",
    fullText:
      'Leading technology companies announced today a groundbreaking collaboration to establish ethical guidelines for artificial intelligence development. The initiative aims to address concerns about AI safety, bias, and transparency.\n\nThe coalition, which includes representatives from major tech firms across North America, Europe, and Asia, will work to create a framework that balances innovation with responsible deployment.\n\n"This is a critical step forward in ensuring that AI technologies benefit humanity while minimizing potential risks," said the spokesperson for the coalition.',
    sentimentScore: 0.75,
    sentimentLabel: "POSITIVE",
  },
  {
    id: "2",
    url: "https://example.com/news/2",
    title: "Market Volatility Continues as Inflation Concerns Grow",
    seenDate: "2023-05-14T15:45:00Z",
    domain: "example.com",
    language: "en",
    sourceCountry: "UK",
    socialImage: "/placeholder.svg?height=400&width=600",
    fullText:
      "Global markets experienced significant turbulence today as new economic data fueled concerns about persistent inflation. Major indices saw declines across the board, with technology and consumer discretionary sectors hit hardest.\n\nAnalysts point to higher-than-expected inflation figures from several major economies as the primary driver of today's sell-off. Central banks are now under increased pressure to accelerate interest rate hikes, potentially slowing economic growth.\n\n\"We're entering a challenging period where policymakers must balance inflation control with maintaining economic momentum,\" noted a senior economist at a leading investment bank.",
    sentimentScore: -0.65,
    sentimentLabel: "NEGATIVE",
  },
  {
    id: "3",
    url: "https://example.com/news/3",
    title: "New Study Reveals Promising Treatment for Chronic Condition",
    seenDate: "2023-05-13T09:15:00Z",
    domain: "example.com",
    language: "en",
    sourceCountry: "CA",
    socialImage: "/placeholder.svg?height=400&width=600",
    fullText:
      'Researchers at a prominent medical institute have published findings suggesting a breakthrough in treating a widespread chronic condition. The study, which followed patients over a five-year period, demonstrated significant improvement in symptoms and quality of life metrics.\n\nThe treatment combines existing medications with a novel therapeutic approach, potentially offering hope to millions of sufferers worldwide. Clinical trials are expected to expand to multiple countries next year.\n\n"While we\'re still in the early stages, these results are extremely encouraging," said the lead researcher. "We\'re cautiously optimistic that this could represent a major advance in how we manage this condition."',
    sentimentScore: 0.82,
    sentimentLabel: "POSITIVE",
  },
  {
    id: "4",
    url: "https://example.com/news/4",
    title: "Environmental Report Highlights Urgent Need for Climate Action",
    seenDate: "2023-05-12T14:20:00Z",
    domain: "example.com",
    language: "en",
    sourceCountry: "DE",
    socialImage: "/placeholder.svg?height=400&width=600",
    fullText:
      'A comprehensive environmental assessment released today emphasizes that the window for effective climate action is narrowing rapidly. The report, compiled by an international team of scientists, details accelerating impacts across ecosystems worldwide.\n\nParticularly concerning are findings related to ocean acidification, biodiversity loss, and extreme weather events, all of which are occurring at rates faster than previously projected. The economic costs of inaction are estimated to be substantial.\n\n"This isn\'t just an environmental issue anymore—it\'s an economic and social imperative," stated one of the report\'s authors. "The data clearly shows that delayed action will result in significantly higher costs and risks."',
    sentimentScore: -0.78,
    sentimentLabel: "NEGATIVE",
  },
  {
    id: "5",
    url: "https://example.com/news/5",
    title: "International Summit Concludes with Trade Agreement",
    seenDate: "2023-05-11T18:00:00Z",
    domain: "example.com",
    language: "en",
    sourceCountry: "FR",
    socialImage: null,
    fullText:
      'Representatives from twelve nations concluded a week-long summit today, signing a preliminary trade agreement aimed at reducing barriers and harmonizing regulations. The pact, which still requires legislative approval in most participating countries, could increase regional trade volume by an estimated 15% over five years.\n\nKey provisions include reduced tariffs on agricultural products, simplified customs procedures, and enhanced protection for intellectual property. Negotiators also established working groups to address digital commerce and environmental standards.\n\n"This balanced agreement reflects years of careful diplomacy and compromise," said the summit chair. "It creates a foundation for sustainable economic growth while respecting each nation\'s sovereignty."',
    sentimentScore: 0.12,
    sentimentLabel: "NEUTRAL",
  },
  {
    id: "6",
    url: "https://example.com/news/6",
    title: "Major Sports League Announces Expansion Teams",
    seenDate: "2023-05-10T12:30:00Z",
    domain: "example.com",
    language: "en",
    sourceCountry: "US",
    socialImage: "/placeholder.svg?height=400&width=600",
    fullText:
      'One of the world\'s premier sports leagues revealed plans today to add two expansion franchises, bringing the total number of teams to thirty-two. The new teams will be located in rapidly growing metropolitan areas that have long sought major professional sports representation.\n\nThe expansion, scheduled to take effect in the 2025-26 season, includes a $500 million investment in community facilities and youth development programs. League officials cited strong fan support and favorable demographic trends as key factors in the decision.\n\n"These vibrant markets have demonstrated exceptional enthusiasm and commitment," the league commissioner announced. "We\'re excited to welcome these communities into our global sports family."',
    sentimentScore: 0.68,
    sentimentLabel: "POSITIVE",
  },
]


import { NewsCard } from "@/components/news-card"
import { fetchNews } from "@/lib/api"

export default async function HomePage() {
  const news = await fetchNews()

  return (
    <main className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Latest News</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {news.map((article) => (
          <NewsCard key={article.id} article={article} />
        ))}
      </div>
    </main>
  )
}


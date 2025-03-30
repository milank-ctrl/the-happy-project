import Image from "next/image"
import Link from "next/link"
import { ArrowLeft, Calendar, Globe } from "lucide-react"
import { fetchNewsById } from "@/lib/api"
import { formatDate } from "@/lib/utils"
import { SentimentBadge } from "@/components/sentiment-badge"

export default async function NewsDetailPage({ params }: { params: { id: string } }) {
  const article = await fetchNewsById(params.id)

  if (!article) {
    return <div className="container mx-auto px-4 py-8">Article not found</div>
  }

  return (
    <main className="container mx-auto px-4 py-8">
      <Link href="/" className="flex items-center text-primary mb-6 hover:underline">
        <ArrowLeft className="mr-2 h-4 w-4" />
        Back to all news
      </Link>

      <article className="max-w-4xl mx-auto">
        <h1 className="text-3xl md:text-4xl font-bold mb-4">{article.title}</h1>

        <div className="flex flex-wrap gap-4 mb-6 text-sm text-muted-foreground">
          <div className="flex items-center">
            <Calendar className="mr-1 h-4 w-4" />
            {formatDate(article.seenDate)}
          </div>
          <div className="flex items-center">
            <Globe className="mr-1 h-4 w-4" />
            {article.domain} • {article.sourceCountry}
          </div>
          <SentimentBadge sentiment={article.sentimentLabel} score={article.sentimentScore} />
        </div>

        {article.socialImage && (
          <div className="mb-6 relative h-[400px] w-full">
            <Image
              src={article.socialImage || "/placeholder.svg"}
              alt={article.title}
              fill
              className="object-cover rounded-lg"
            />
          </div>
        )}

        <div className="prose prose-lg max-w-none">
          {article.fullText.split("\n").map((paragraph, index) => (
            <p key={index}>{paragraph}</p>
          ))}
        </div>

        <div className="mt-8 pt-6 border-t">
          <Link
            href={article.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow hover:bg-primary/90"
          >
            Read original article
          </Link>
        </div>
      </article>
    </main>
  )
}


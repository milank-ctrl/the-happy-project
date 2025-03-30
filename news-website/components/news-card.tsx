import Link from "next/link"
import Image from "next/image"
import { Calendar, ExternalLink } from "lucide-react"
import { Card, CardContent, CardFooter } from "@/components/ui/card"
import { SentimentBadge } from "@/components/sentiment-badge"
import { formatDate } from "@/lib/utils"
import type { NewsArticle } from "@/lib/types"

interface NewsCardProps {
  article: NewsArticle
}

export function NewsCard({ article }: NewsCardProps) {
  return (
    <Card className="overflow-hidden flex flex-col h-full">
      {article.socialImage ? (
        <div className="relative h-48 w-full">
          <Image src={article.socialImage || "/placeholder.svg"} alt={article.title} fill className="object-cover" />
        </div>
      ) : (
        <div className="h-48 bg-muted flex items-center justify-center">
          <p className="text-muted-foreground">No image available</p>
        </div>
      )}

      <CardContent className="pt-6 flex-grow">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm text-muted-foreground">{article.domain}</span>
          <SentimentBadge sentiment={article.sentimentLabel} score={article.sentimentScore} />
        </div>

        <Link href={`/news/${article.id}`}>
          <h3 className="text-xl font-bold mb-2 hover:text-primary transition-colors">{article.title}</h3>
        </Link>

        <p className="text-muted-foreground line-clamp-3 mb-4">{article.fullText.substring(0, 150)}...</p>

        <div className="flex items-center text-sm text-muted-foreground">
          <Calendar className="mr-1 h-4 w-4" />
          {formatDate(article.seenDate)}
        </div>
      </CardContent>

      <CardFooter className="pt-0 flex justify-between">
        <Link href={`/news/${article.id}`} className="text-primary hover:underline text-sm">
          Read more
        </Link>

        <Link
          href={article.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm flex items-center text-muted-foreground hover:text-foreground"
        >
          Source <ExternalLink className="ml-1 h-3 w-3" />
        </Link>
      </CardFooter>
    </Card>
  )
}


import { TrendingDown, TrendingUp, Minus } from "lucide-react"
import { cn } from "@/lib/utils"

interface SentimentBadgeProps {
  sentiment: "NEGATIVE" | "POSITIVE" | "NEUTRAL"
  score?: number
  showScore?: boolean
}

export function SentimentBadge({ sentiment, score, showScore = false }: SentimentBadgeProps) {
  const getBadgeColor = () => {
    switch (sentiment) {
      case "POSITIVE":
        return "bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400"
      case "NEGATIVE":
        return "bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400"
      case "NEUTRAL":
      default:
        return "bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-400"
    }
  }

  const getIcon = () => {
    switch (sentiment) {
      case "POSITIVE":
        return <TrendingUp className="h-3 w-3 mr-1" />
      case "NEGATIVE":
        return <TrendingDown className="h-3 w-3 mr-1" />
      case "NEUTRAL":
      default:
        return <Minus className="h-3 w-3 mr-1" />
    }
  }

  return (
    <span className={cn("inline-flex items-center px-2 py-1 rounded-full text-xs font-medium", getBadgeColor())}>
      {getIcon()}
      {sentiment.charAt(0) + sentiment.slice(1).toLowerCase()}
      {showScore && score !== undefined && ` (${score.toFixed(2)})`}
    </span>
  )
}


import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const ArticleTitle: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const title = fileData.frontmatter?.title
  const subtitle = fileData.frontmatter?.description
return (
    <header class="article-title-block">
      <h1 class="article-title">{title}</h1>
      {subtitle && <p class="article-subtitle">| {subtitle}</p>}
    </header>
  )
}

ArticleTitle.css = `
.article-title {
  margin: 2rem 0 0 0;
}

.article-subtitle {
  
  font-size: 1.5rem;
  font-weight: 400;
  color: var(--gray);
  margin: 2rem 0 0 0;
}
`
export default (() => ArticleTitle) satisfies QuartzComponentConstructor

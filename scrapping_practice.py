#https://www.wired.com/story/can-ai-built-to-benefit-humanity-also-serve-military/
from newspaper import Article

url = 'https://www.wired.com/story/can-ai-built-to-benefit-humanity-also-serve-military/'
article = Article(url)
article.download()
article.parse()
print(article.text)
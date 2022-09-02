import scrapy


## for scrawl in terminal try:- 'scrapy crawl flipkart'
### to store in json file try this :- 'scrapy crawl flipkart -O flipkart.json'

class Flipkart_scraper(scrapy.Spider):
    name = 'flipkart'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
    start_urls = ['https://www.flipkart.com/search?q=baby%20products&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
    
    def parse(self, response):
        for products in response.css('div._4ddWXP'):
            try:
                yield {
                'product_name': products.css('a.s1Q9rs').attrib['title'],
                'price' : products.css('div._30jeq3::text').get(),
                'link': f"https://www.flipkart.com{products.css('a.s1Q9rs').attrib['href']}"
            }
            except:
                pass

            
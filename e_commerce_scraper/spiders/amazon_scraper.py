import scrapy


## for scrawl in terminal try:- 'scrapy crawl amazon'
### to store in json file try this :- 'scrapy crawl amazon -O amazon.json'

class Amazon_scraper(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?k=baby+products&crid=2XB2C6FPJA01N&sprefix=baby+products%2Caps%2C309&ref=nb_sb_noss_1']
    
    def parse(self, response):
        for products in response.css('div.s-card-border'):
            try:
                yield {
                'product_name': products.css('span.a-size-base-plus::text').get(),
                'price' : products.css('span.a-offscreen::text').get(),
                'link': f"https://www.amazon.com{products.css('a.a-link-normal').attrib['href']}"
            }
            except:
                pass

            
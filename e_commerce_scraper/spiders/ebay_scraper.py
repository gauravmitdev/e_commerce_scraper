import scrapy


## for scrawl in terminal try:- 'scrapy crawl ebay'
### to store in json file try this :- 'scrapy crawl ebay -O ebay.json'

class Ebay_scraper(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=baby+products&_sacat=0']
    
    def parse(self, response):
        for products in response.css('li.s-item__pl-on-bottom'):
            try:
                yield {
                'product_name': products.css('div.s-item__title span::text').get(),
                'price' : products.css('span.s-item__price::text').get(),
                'link': products.css('a.s-item__link').attrib['href']
            }
            except:
                pass

            
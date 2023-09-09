import scrapy

class MoviesSpider(scrapy.Spider):
    name='movies'
    start_urls=['https://bloghorror.com/']
    
    def parse(self, response):
        with open('movies.html', 'w', encoding='utf-8') as f:
            f.write(response.txt)
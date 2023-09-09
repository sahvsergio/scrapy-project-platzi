import scrapy


class SavantSpider(scrapy.Spider):
    name='savant'
    start_urls=['https://www.savant-international.com']
    
    
    def parse(self,response):
        title=response.xpath('//h1[@class="titulo-principal"]').get()
        print(title)
        #links=response.xpath('//a[@class="icono-redes"]/*/@href').getall()
        #print(links)
    
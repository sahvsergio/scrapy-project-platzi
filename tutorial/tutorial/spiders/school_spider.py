import scrapy

class SchoolSpider(scrapy.Spider):
    name='school'
    start_urls=['https://www.lfrm.edu.co']
    
    def parse(self, response):
        with open('school.html','w', encoding='utf-8') as f:
            f.write(response.txt)
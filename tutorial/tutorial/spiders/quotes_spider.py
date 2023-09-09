import scrapy
#titulo= //h1/a/text()
#citas= //span[@class='text' and @itemprop='text']/text()
#top ten tags= //div[contains(@class='tags-box')]//span[@class='tag-item']/a/text()
#next_page_button=//ul[@class="pager"]//li[@class="next"]/a/@href').get()

#We need to create a class with the same name as the file name
class QuotesSpider(scrapy.Spider):
    name='Quotes'
    start_urls=['http://quotes.toscrape.com/page/1']
    #USUALLY REPLACES USING  SCFAPY CRAWL QUOTES -o quotes.json
    custom_settings={
        'FEED_URI':'quotes.json',
        'FEED_FORMAT':'json',
        'CONCURRENT_REQUESTS':24,
        'MEMUSAGE_LIMIT_MB':2048,
        'MEMUSAGE_NOTIFY_MAIL':'sergioandresherrera@gmail.com',
        'ROBOTSTXT_OBEY':True,
        'USER_AGENT':'Pepito Martinez',
        'FEED_EXPORT_ENCODING':'utf-8'
    
        
    }   
    def parse_only_quotes(self, response,**kwargs):
        if kwargs:
           quotes=kwargs['quotes']
        quotes.extend(response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall() ) 
        next_page_button_link=response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,callback=self.parse_only_quotes, cb_kwargs={'quotes':quotes}) 
        else:
            yield {'quotes':quotes}
                 
    
    """
    def parse(self,response):
        with open('resultados.html','w',encoding='utf-8') as f:
            f.write(response.text)
       """
    def parse(self, response):
        title=response.xpath('//h1/a/text()').get()
        quotes=response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_tags=response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
               
        top=getattr(self,'top',None)
        if top:
            top=int(top)
            top_tags=top_tags[:top]
        yield {
            'title':title,
            
            #'quotes':quotes,
            
            'top_tags':top_tags

        }
        next_page_button_link=response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,callback=self.parse_only_quotes, cb_kwargs={'quotes':quotes}) #clicks on the next 
        
        """"
        print('*'*10)
        print('\n\n\n') 
        title=response.xpath('//h1/a/text()').get()
        print(f'título:{title}')#because it is only one, in case of a list , 
        #print(response.status, response.headers)
        print('\n\n')
        quotes=response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        
        for quote in quotes:
            print(f'-{quote}')
        top_ten_tags=response.xpath('//div[contains(@class"tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('Top Ten Tags')
        for tag in top_ten_tags:
            print(f'-{tag}')
            print('\n \n')
            print('*'*10)
            print('\n \n')
            
            
            """
            
            
        
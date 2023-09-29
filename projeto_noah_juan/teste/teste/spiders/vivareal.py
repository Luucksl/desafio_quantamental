import scrapy


class VivarealSpider(scrapy.Spider):
    name = "vivareal"
    allowed_domains = ["www.vivareal.com.br"]
    start_urls = ["https://www.vivareal.com.br/venda/?pagina=2"]

    def parse(self, response):
        for card in response.xpath("//div[@class='property-card__content']"):
            yield {
                'name' : response.xpath('//span[@class="property-card__title js-cardLink js-card-title"]').get(),
                'price' : response.xpath('//div[@class="property-card__price js-property-card-prices js-property-card__price-small"]/p/text()').get()
            }

# criar projeto
scrapy startproject nome_projeto

# criar layout spyder
scrapy genspyder nome_spyder url

# executar spyder
scrapy crawl nome_spyder
import scrapy


class Bbc_Urdu(scrapy.Spider):
    name = 'bbc_urdu'

    start_urls = ['https://www.bbc.com/urdu/topics/cjgn7n9zzq7t?page=1']

    def parse(self, response):

        images = response.xpath(
            "//div[@class='promo-image']//img/@src").getall()

        next_page = response.xpath(
            "//a[@aria-labelledby='pagination-next-page']/@href").get()
        if next_page:
            yield scrapy.Request(
                url="https://www.bbc.com/urdu/topics/cjgn7n9zzq7t" + next_page,
                callback=self.parse)
        for title, date, image in zip(images):
            yield {
                "Image": image,
            }

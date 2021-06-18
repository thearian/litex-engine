import scrapy
from datetime import datetime
import json

from clean import clean_text, is_binary_string

class Crawler(scrapy.Spider):
    name = 'Crawler_Spider'
    start_urls = ["https://en.wikipedia.org/wiki/Human"]

    def parse(self, res):
        time_obj = datetime.now()
        current_time = [
            str(time_obj.year),
            str(time_obj.month),
            str(time_obj.day),
            str(time_obj.hour),
            str(time_obj.minute),
            str(time_obj.second),
        ]

        new_article = {
            "title": clean_text(res.css('h1 ::text').extract_first()),
            "text": "",
            "extractedAt": "-".join(current_time)
        }

        for p_text in res.css('p'):
            text = p_text.css('::text').extract_first()
            text = clean_text(text)
            yield {
                "p": text
            }
            new_article["text"] += text

        if len(new_article["text"]) > 0 and is_binary_string(new_article["text"]):
            title = "-".join(current_time)
            if len(new_article["title"]) > 0:
                title = new_article["title"]
            database = open("data/"+ title +".json","at")
            data = json.dumps(new_article, indent="     ")
            database.write(data)
        
        for linked_sites in res.css('a'):
            link = linked_sites.css('::attr(href)').extract_first()
            if link:
                yield scrapy.Request(
                    res.urljoin(link),
                    callback=self.parse
                )
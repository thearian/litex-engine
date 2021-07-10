import scrapy
from datetime import datetime
import json

from helper import clean_text, is_binary_string, is_http_url
import database
from trim import trim_text

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

        new_source = {
            "title": clean_text(res.css('h1 ::text').extract_first()),
            "text": "",
            "extractedAt": "-".join(current_time)
        }

        for p_text in res.css('p'):
            text = p_text.css('::text').extract_first()
            text = clean_text(text)
            new_source["text"] += text

        if len(new_source["text"]) > 10 and is_binary_string(new_source["text"]):
            title = "-".join(current_time)
            if len(new_source["title"]) > 0:
                title = new_source["title"]
            database.save(new_source, "data/sources/"+title)

            text = {
                "source": res.request.url,
                "title": title,
                "texts": trim_text(new_source["text"]),
                "trimedAt": "-".join(current_time),
            }
            database.save(text, "data/texts/"+title)
        
        for linked_sites in res.css('a'):
            link = linked_sites.css('::attr(href)').extract_first()
            if link and is_http_url(link):
                yield scrapy.Request(
                    res.urljoin(link),
                    callback=self.parse
                )
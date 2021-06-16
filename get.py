from urllib import request
import re

def clean_html(raw_html):
    cleaner = re.compile('<.*?>')
    return re.sub(cleaner, '', raw_html)

def get_paragraphs(raw_html):
    p_elements = re.findall("<p>.*</p>", str(raw_html))
    paragraphs = ""
    for p in p_elements:
        paragraphs += clean_html(p)
    return paragraphs.replace('\\n', '\n').replace('\\t', '\t'.replace('\\s', '\s'))

def get_text_of_webpage(url):
    html = request.urlopen(url).read()
    return get_paragraphs(html)
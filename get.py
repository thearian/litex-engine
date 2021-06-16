from urllib import request
import re
from os import system

def clean_html(raw_html):
    cleaner = re.compile('<.*?>')
    return re.sub(cleaner, '', raw_html)

def get_paragraphs(raw_html):
    p_elements = re.findall("<p>.*</p>", str(raw_html))
    paragraphs = ""
    for p in p_elements:
        paragraphs += clean_html(p)
    return paragraphs.replace('\\n', '\n').replace('\\t', '\t'.replace('\\s', '\s'))

url = input("URL: ")
html = request.urlopen(url).read()

paragraphs = get_paragraphs(html)
open("file.txt","wt").write(paragraphs)

system("py trim.py")
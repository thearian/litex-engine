from flask import Flask
from flask import request
import trim
import get

app = Flask(__name__)

def convert_to_dict(converting_list):
    litexes = {}
    for i, litex in enumerate(converting_list):
        litexes[i] = litex
    return litexes

@app.route('/trim/text')
def route_trim_text():
    text = request.args.get('text')
    trimed = trim.trim_text(text)
    return convert_to_dict(trimed)

@app.route('/trim/url')
def route_trim_url():
    url = request.args.get('url')
    print(url)
    text = get.get_text_of_webpage(url)
    print(text[0:100])
    trimed = trim.trim_text(text)
    print(trimed)
    return convert_to_dict(trimed)
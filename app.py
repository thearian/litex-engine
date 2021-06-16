from flask import Flask
from flask import request
import trim

app = Flask(__name__)

@app.route('/trim')
def route_trim():
    text = request.args.get('text')
    trimed = trim.trim_text(text)
    # convert list to dictionary
    litexes = {}
    for i, litex in enumerate(trimed):
        litexes[i] = litex
    return litexes
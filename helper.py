import re
from sys import argv

def clean_backslash(text):
    cleaned = text.replace('\\n', ' ').replace('\\t', ' ').replace('\\s', ' ')
    return cleaned

cleaner = re.compile('<.*?>')
def clean_html(raw_html):
    html_cleaned = re.sub(cleaner, '', str(raw_html))
    return html_cleaned

def clean_text(text):
    return clean_backslash(
        clean_html(text)
    )

if len(argv) > 1:
    print(
        clean_html(argv[1])
    )

def is_binary_string(bytes):
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    return bool(bytes.translate(textchars))

def is_http_url(url):
    result = re.match('^(https?:\\/\\/)?((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|((\\d{1,3}\\.){3}\\d{1,3}))(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*(\\?[;&a-z\\d%_.~+=-]*)?(\\#[-a-z\\d_]*)?$',
        url
    )
    return result != None
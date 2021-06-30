# Litex Engine
Litex python text analyze for compressing and trimming sources to small conclusions


## Start working (installation)
[Flask full documentaion for installation](https://flask.palletsprojects.com/en/2.0.x/installation/)
### 1. Python version 3.6 or newer
It is recommended to use the latest version of Python. Flask supports Python 3.6 and newer.

### 2. Activate the enviroment
```
venv\Scripts\activate
```

### 3. Install Flask
```
pip install flask
```


## Crawler
The crawler will visit the website it is given at `crawler.py` file and look for any website links and indexs them.\
The current way of saving the results is *JSON fiels*. So you need to make the `data/` directory.
```bash
mkdir data
cd data
mkdir sources
mkdir texts
```
For runnging the crawler first install scrapy and then run `crawler.py` spider.
```bash
pip install scrapy
```
```bash
scrapy runspider crawler.py
```
## Develop
### Testing Trim
```bash
py trim.py "mytext"
```
### Running Flask
The server file is `app.py`. This name is **vital** to skip setting the flask enviroment variables.\
For starting the server run
```
flask run
```
and the server will be on http://localhost:5000

## Documentaion
### Requests
|url       |query parameters  |
| -------- | ---------------- |
|/trim/text|text: String      |
|/trim/url |url: String       |

### Responces types
```typescript
{
    subjects: [string,number],
    paragraph: string,
    weight: number,
} 
```
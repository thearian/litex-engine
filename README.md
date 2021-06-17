# Litex Engine
Litex python text analyze for compressing and trimming articles to small conclusions


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
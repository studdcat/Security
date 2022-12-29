# Web Server with Python

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/admin')
def admin():
   return 'This is admin!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
```
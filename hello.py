from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page\n'

@app.route('/hello')
def hello():
    return '''\
Hello, Flask!
'''

@app.route('/version')
def version():
    import sys
    return sys.version

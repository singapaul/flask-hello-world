from flask import Flask
from flask import request
from completionCall import call_playlist_prompt
 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/demo')
def hello_world():
    return 'Hello, Paul'

@app.route('/post-json', methods=['POST'])
def handle_json_data():
    return call_playlist_prompt()

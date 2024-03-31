from flask import Flask
from flask import request
from dotenv import dotenv_values
import openai
from completionCall import call_playlist_prompt
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()

my_id = os.getenv("API_KEY")



# config = dotenv_values('.env')
openai.api_key = my_id


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

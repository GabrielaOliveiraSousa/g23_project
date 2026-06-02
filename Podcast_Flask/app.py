from flask import Flask
from datafile import filename        
import subs.index_subs as indexSubs

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'  

path = filename + 'DadaBase_Podcast.db'

@app.route("/", methods=["POST", "GET"])
def index():
    return indexSubs.index(path)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
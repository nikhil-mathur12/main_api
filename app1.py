from flask import Flask, jsonify, request
import json
from urllib.request import urlopen
app = Flask(__name__)


@app.route('/start_scraper', methods=['POST'])
def update_record():
    body = request.get_json()
    print(body)
    url = body['url']
    response = urlopen(url)
    data_json = json.loads(response.read())
    msg = {"message":"Scraping is under process "+url}
    return jsonify(msg)


if __name__ == '__main__':
   app.run()
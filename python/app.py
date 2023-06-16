from flask import Flask, request, jsonify
from scraper import scrape_amazon_page

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    url = request.args.get('url')
    if url:
        data = scrape_amazon_page(url)
        return jsonify(data)
    else:
        return jsonify(error='No URL provided')

if __name__ == '__main__':
    app.run()

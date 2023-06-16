from flask import Flask, jsonify
from scraper import scrape_website

app = Flask(__name__)

@app.route('../src/views/HomePage.vue')
def get_website_title():
    title = scrape_website()
    return jsonify({'title': title})

if __name__ == '__main__':
    app.run()

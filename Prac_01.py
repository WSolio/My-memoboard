import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
   return render_template('posting_page.html')

@app.route('/post', methods=['POST'])
def saving():
    # 클라이언트로부터 데이터를 받는 부분
    url_receive = request.form['url_give']
    image_receive = request.form['image_give']
    author_receive = request.form['author_give']
    # meta tag를 스크래핑 하는 부분

    url = 'http://www.asiatime.co.kr/news/articleView.html?idxno=259944'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')


    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    print(og_image, og_title, og_description)

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    print(url_image, url_title, url_description)



    # mongoDB에 넣는 부분

    return jsonify({'result': 'success'})
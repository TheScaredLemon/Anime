from flask import Flask, render_template, request, redirect, flash, jsonify
from models import db, Anime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

API_BASE_URL = "https://api.myanimelist.net/v2"
API_TOKEN = "your_access_token"

@app.route('/')
def show_anime_list():
    animes = Anime.query.all()
    return render_template('anime_list.html', animes=animes)

@app.route('/anime/<int:anime_id>')
def show_anime_detail(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    return render_template('anime_detail.html', anime=anime)

@app.route('/api/anime')
def get_anime_from_api():
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(f'{API_BASE_URL}/anime', headers=headers, params={'q': 'one', 'limit': 10})
    data = response.json()
    for item in data['data']:
        anime = Anime(
            id=item['node']['id'],
            title=item['node']['title'],
            synopsis=item.get('node', {}).get('synopsis', ''),
            score=item.get('node', {}).get('mean', 0),
            image_url=item.get('node', {}).get('main_picture', {}).get('medium', '')
        )
        db.session.add(anime)
    db.session.commit()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

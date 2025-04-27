from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.jikan.moe/v4/anime/54595/episodes"
    response = requests.get(url)
    data = response.json()

    a = ""
    for episode in data["data"]:
        score = episode.get("score", "Немає оцінки")
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {score}</p>"
    return a

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from model import recommend_movies, get_all_titles

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    movies = get_all_titles()

    if request.method == 'POST':
        movie = request.form.get('movie')
        recommendations = recommend_movies(movie)

    return render_template(
        'index.html',
        recommendations=recommendations,
        movies=movies
    )

if __name__ == '__main__':
    app.run(debug=True)
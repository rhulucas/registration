from fastapi import FastAPI
from movie import Movie

app =FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.get("/movie/{movie_name}")
def get_movieview_by_name(movie_name: str):
    results = []
    if movie_name:
        movies = Movie(movie_name)
        movies.youtube_search(max_result=10)
        return movies._review_videos
    return results


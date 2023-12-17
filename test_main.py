from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"} 

def test_get_movieview_by_name():
    response = client.get("/movie/test_movie")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
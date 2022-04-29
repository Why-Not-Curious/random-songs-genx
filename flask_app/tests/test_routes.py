from flask import Flask
from flask_app.main.routes import configure_routes

#  create app client for sensinf test requests
def create_client():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    return client

# test response status, type and data for valid user name
def test_random_songs_valid():
    client = create_client()
    url = '/random_songs/5'
    response =  client.get(url)
    assert response.status_code == 200
    assert b'title' in response.get_data()
    assert response.content_type == 'application/json'



def test_main_app(client):
    response = client.get('/test')
    data = response.json()
    assert response.status_code == 200
    assert data['message'] == "Hello World test"
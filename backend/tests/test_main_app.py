def test_main_app_index_route(client):
    response = client.get('/')
    data = response.json()
    assert response.status_code == 200
    assert data['loc'] == 'root'


def test_main_app_test_route(client):
    response = client.get('/test')
    data = response.json()
    assert response.status_code == 200
    assert data['message'] == "Hello World test"
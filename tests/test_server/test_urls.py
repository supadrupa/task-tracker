def test_get_docs(client):
    response = client.get('/api/docs/')
    assert response.status_code == 200

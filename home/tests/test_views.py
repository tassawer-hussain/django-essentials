def test_home_view(client):
    # Test the Get endpoint of home
    response = client.get(path='/')
    assert response.status_code == 200
    assert 'Welcome to SmartNotes!' in str(response.content)
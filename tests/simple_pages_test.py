def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Hello, Class!" in response.data

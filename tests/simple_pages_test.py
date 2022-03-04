
def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Index Page"


def test_request_git(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Git"

def test_request_pyflask(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Testing with pytest"

def test_request_cicd(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Continuous Integration/Continuous Deployment"

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Docker"
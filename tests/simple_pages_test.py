
def test_request_index(client):
    """This makes the index page"""
    response = client.get("simple_pages/templates/index.html")
    assert b"Home" in response.data


#def test_request_git(client):
#    """This tests the index page"""
 #   response = client.get("/")
  #  assert b"Git" in response.data

#def test_request_pyflask(client):
 #   """This tests the pyflask page"""
  #  response = client.get("/app/simple_pages/templates/pyflask.html")
 #   assert b"Testing with pytest" in response.data

#def test_request_cicd(client):
#    """This tests the cicd page"""
  #  response = client.get("/")
 #   assert b"Continuous Integration/Continuous Deployment"

#def test_request_docker(client):
 #   """This tests the docker page"""
 #   response = client.get("/")
  #  assert b"Docker"


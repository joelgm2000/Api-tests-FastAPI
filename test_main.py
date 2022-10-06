from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

       
def test_read_isPrimo1():
    response = client.get("/isPrimo/2")
    assert response.status_code == 200
    assert response.json() == {"changed": True, "msg": "Es primo"}   


def test_read_isPrimo2():
    response = client.get("/isPrimo/-2")
    assert response.status_code == 200
    assert response.json() == {"changed": False, "msg": "No es primo"} 

def test_read_isPrimo3():
    response = client.get("/isPrimo/f")
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["path","is_primo_id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}   

def test_read_isPrimo4():
    response = client.get("/isPrimo/1")
    assert response.status_code == 200
    assert response.json() == {"changed": False, "msg": "No es primo"}   
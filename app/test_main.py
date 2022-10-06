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


def test_read_fibonacci():
    response = client.get("/fibonacci/{item_id}?pos=7")
    assert response.status_code == 200
    assert response.json() == {"fibonacci": 8}

def test_fibonacci_pos_menor_1():
    response = client.get("/fibonacci/{item_id}?pos=0")
    assert response.status_code == 200
    assert response.json() == {"Error": "Posición inválida"}

def test_fibonacci_pos_letra():
    response = client.get("/fibonacci/{item_id}?pos=n")
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["query","pos"],"msg":"value is not a valid integer","type":"type_error.integer"}]}

def test_fibonacci_pos_decimal():
    response = client.get("/fibonacci/{item_id}?pos=5.2")
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["query","pos"],"msg":"value is not a valid integer","type":"type_error.integer"}]}

def test_fibonacci_url():
    response = client.get("/fibonacci/6")
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["query","pos"],"msg":"field required","type":"value_error.missing"}]} 
    
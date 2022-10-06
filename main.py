from typing import Union
from math import sqrt
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def read_root():
    
    return {"msg": "Hello World"}

@app.get("/isPrimo/{is_primo_id}")
async def primo(is_primo_id:int):
    if is_primo_id>1:
        s=int(is_primo_id/2)
        for i in range(2,s+1):
            if is_primo_id%i==0:
                return {"changed": False, "msg": "No es primo"}
                break
        return {"changed": True, "msg": "Es primo"}
    else:
        return {"changed": False, "msg": "No es primo"}
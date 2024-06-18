from fastapi import FastAPI
import string
import random


app = FastAPI()


@app.get('/')
async def index():
    xstr = ''.join(random.choice(string.ascii_lowercase, k=5))
    return {'data': xstr}


@app.get('/items/{arg}')
async def read(arg):
    return {"item_id": arg}

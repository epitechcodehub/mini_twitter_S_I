import sys
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class Post:
    def __init__(self, com, post):
        self.com = com
        self.tab = []
        self.post = post;

    def new_com(self, com):
        self.tab.append(com)

def main():
    read_root()
    read_item()

main()


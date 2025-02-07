from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class Post:
    def __init__(self, post):
        self.tab = []
        self.post = post;

    def new_com(self, com):
        self.tab.append(com)
    def disp_com(self):
        for i in range(len(self.tab)):
            print(self.tab[i])
    def disp(self):
        print(self.post)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

def main():
    my_post = Post("itit")
    my_post.disp()
    my_post.new_com("tatat")
    my_post.disp_com()

main()


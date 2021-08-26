
from typing import Optional
from fastapi import FastAPI



app = FastAPI()


@app.get("/user/{user_id}/item/{item_id}")
async def read_item(user_id:int,item_id :str,q : Optional[str]=None ,short:bool =False):
    item = {"owner_id":user_id,"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is am amazing item that have long descriprtion"})
    return item


   


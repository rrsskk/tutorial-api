
from typing import Optional
from fastapi import FastAPI,Query


app = FastAPI()


@app.get("/items/")
async def read_item(q:str=Query("fixedquery",min_length=3,)):
    result= {"item_id":[{"item_id":"Foo"},{"item_id":"Bar"}]} 
    if q:
        result.update({"q":q})

        return result


   


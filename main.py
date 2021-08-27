
from typing import Optional
from fastapi import FastAPI,Query


app = FastAPI()


@app.get("/items/")
async def read_item(q:Optional[str]=Query(None,max_length=50)):
    result= {"item_id":[{"item_id":"Foo"},{"item_id":"Bar"}]} 
    if q:
        result.update({"q":q})

        return result


   


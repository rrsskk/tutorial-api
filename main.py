
from typing import Optional
from fastapi import FastAPI,Query


app = FastAPI()


@app.get("/items/")
async def read_item(q:Optional[str]=Query(None,title="Query String",
description="Query string for the item to search in database that have good match",min_length=3)):
    
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q": q})
    return result


    


   


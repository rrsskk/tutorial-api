
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/items/")
async def create_item(q:Optional[str]=None):
    result= {"item_id":[{"item_id":"Foo"},{"item_id":"Bar"}]} 
    if q:
        result.update({"q":q})

        return result


   


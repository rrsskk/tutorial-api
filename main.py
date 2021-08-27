
from typing import Optional
from fastapi import FastAPI,Path,Query


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id:int=Path(...,title="The id of item to get"),
    q:Optional[str]=Query(None,alias="item-query")):
    
    result = {"item_id":item_id}
    if q:
        result.update({"q": q})
    return result


    


   


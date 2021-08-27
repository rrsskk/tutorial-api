
from typing import Optional
from fastapi import FastAPI,Query


app = FastAPI()


@app.get("/items/")
async def read_item(q:Optional[str]=Query(None,title="item_query",description="This is matched query parameter",
alias="item-query",min_length=3,max_length=50,regex="^item_query$",deprecated=True)):
    
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q": q})
    return result


    


   


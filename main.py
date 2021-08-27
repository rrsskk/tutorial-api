
from typing import Optional,List
from fastapi import FastAPI,Query


app = FastAPI()


@app.get("/items/")
async def read_item(q:List=Query([])):
    
    query_item ={"q":q}

    return query_item


   


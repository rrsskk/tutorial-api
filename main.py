
from typing import Optional,List
from fastapi import FastAPI,Body
from pydantic import BaseModel


app = FastAPI()

class Item (BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float] = None
    tags:List[str]=[]




@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item):
    
    result = {"item_id": item_id,"item":item}
    
    
    return result


    


   


from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

class Item (BaseModel):
    name : str
    description: Optional[str] = None
    price : float
    tax : Optional[float] = None

app = FastAPI()


@app.post("/item/{item_id}")
async def create_item(item_id:int,item:Item):
    return {"item_id":item_id,**item.dict()} 
     


   


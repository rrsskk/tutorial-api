from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

class Item (BaseModel):
    name : str
    description: Optional[str] = None
    price : int
    tax : Optional[float] = None

app = FastAPI()


@app.post("/item/")
async def create_item(item:Item):

    return item


   


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
  item_dict = item.dict()
  if Item.tax:
    price_with_tax = Item.tax + Item.price
    item_dict.update({"price_with_tax":price_with_tax})
      
    return item_dict 
     


   


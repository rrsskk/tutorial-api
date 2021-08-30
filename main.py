
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field


app = FastAPI()

class Item (BaseModel):
    name :str = Field(...,example="Foo")
    description: Optional[str]= Field(None,example="Very nice")
    price: float = Field(...,example="56.0")
    tax:Optional[float]= Field(None,example="20.3")

    
    
@app.put("/item/{item_id}")
async def update_items(item_id:int,item:Item):
    
    result = {"item_id":item_id,"item":item}
    return result


    


   


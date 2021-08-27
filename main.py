
from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel,Field


app = FastAPI()

class Item (BaseModel):
    name:str
    description:Optional[str]=Field(None,title="The description of item",max_length=1000)
    price:float
    tax:Optional[float]=Field(...,gt=0,description="The price must be greater than zero")




@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item= Body(...,embed=True)):
    
    result = {"item_id": item_id,"item":item}
    
    
    return result


    


   


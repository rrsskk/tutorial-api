
from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel


app = FastAPI()

class Item (BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None




@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item= Body(...,embed=True)):
    
    result = {"item_id": item_id,"item":item}
    
    
    return result


    


   


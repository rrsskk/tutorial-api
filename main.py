
from typing import Optional
from fastapi import FastAPI,Body
from pydantic import BaseModel


app = FastAPI()

class Item (BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None

class User(BaseModel):
    username: str
    full_name:Optional[str]=None


@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item,user:User,importance:int= Body(...,gt=0),q:Optional[str]=None):
    
    result = {"item_id": item_id,"item":item,"user":user,"importance":importance}
    if q:
        result.update({"q":q})
    
    return result


    


   


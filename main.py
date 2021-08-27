
from typing import Optional
from fastapi import FastAPI,Path
from pydantic import BaseModel


app = FastAPI()

class item (BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None

@app.put("/items/{item_id}")
async def update_item(*,
item_id: int=Path(...,title="The id of item to get",ge=0,le=100),
    q:Optional[str]=None,item:Optional[item]=None):
    
    result = {"item_id": item_id}
    if q:
         result.update({"q": q})
    if item:
        result.update({"item":item})
    return result


    


   


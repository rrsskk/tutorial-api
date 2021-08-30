
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item (BaseModel):
    name :str
    description: Optional[str]= None
    price: float
    tax:Optional[float]=None

    class config:
        schema_extra = {
            "example":{
                "name":"Foo",
                "description":"very nice item",
                "price":"20.6",
                "tax":"2.4",

            }
        }
    


@app.put("/item/{item_id}")
async def update_items(item_id:int,item:Item):
    
    result = {"item_id":item_id,"item":item}
    return result


    


   


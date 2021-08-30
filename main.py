
from typing import Optional,Set,List
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl


app = FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name:str

class Item (BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float] = None
    tags:Set[str]= set()
    image: Optional[List[Image]] = None



class Offer (BaseModel):
    name :str
    description: Optional[str]=None
    price:float
    item:List[Item]

@app.post("/offer/")
async def create_offer(offer:Offer):
    
    return offer


    


   


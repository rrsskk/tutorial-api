
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl


app = FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name:str




@app.post("/offer/")
async def create_mutiple_images(image:List[Image]):
    
    return image


    


   


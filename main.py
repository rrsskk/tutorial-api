
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl


app = FastAPI()






@app.post("/index-weights/")
async def create_index_weights(weights:Dict[int,float]):
    
    return weights


    


   

